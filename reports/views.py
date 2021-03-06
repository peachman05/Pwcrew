from django.shortcuts import render
import json
import csv
from django.http import Http404, HttpResponseRedirect, HttpResponse

from datetime import date
from data.models import *

def AD_date_to_BD_str(dateObj): # change AD to BD as string(ค.ศ. -> พ.ศ.) date -> d/m/Y (str)
    # import pdb; pdb.set_trace()
    if isinstance(dateObj, date):
        AD_str = dateObj.strftime('%d/%m/%Y') #  date to str
    elif isinstance(dateObj, str) and dateObj: # check is string and not empty
        AD_str = dateObj
    else:
        return ''
    # change AC year str to BC str
    d, m, y = AD_str.split("/",2)
    BD_y = str(int(y) + 543 )
    BD_str = d+'/'+m+'/'+BD_y 

    
    return BD_str

# Create your views here.
# doesn't use graph view*****
def graph(request):
    # my_dict = {'test' : '12345', 'arr' : [1,2,3]}
    # json_data = json.dumps(my_dict)
    department_list = ['ฝ่ายบริหาร',
                       'กลุ่มสาระการเรียนรู้วิทยาศาสตร์',
                       'กลุ่มสาระการเรียนรู้คณิตศาสตร์',
                       'กลุ่มสาระการเรียนรู้ศิลปะ',
                       'กลุ่มสาระการเรียนรู้ภาษาไทย',
                       'กลุ่มสาระการเรียนรู้ภาษาต่างประเทศ',
                       'กลุ่มสาระการเรียนรู้สังคมศึกษา ศาสนา และวัฒนธรรม',
                       'กลุ่มสาระการเรียนรู้การงานอาชีพและเทคโนโลยี',
                       'กลุ่มสาระการเรียนรู้สุขศึกษาและพลศึกษา',
                       'กิจกรรมพัฒนาผู้เรียน'
                       
                       ]

    checklist = request.POST.getlist('checks[]')
    # print("ddafa")
    # print(checklist)
    temp_dict = {}



    if len(checklist) > 0:
        ######  RANK
            ### concat string
        str_temp = ""
        for ind, each_ch in enumerate(checklist):
            if ind == 0:
                str_temp += " department = " + "'" + department_list[int(each_ch)] + "'" 
            else:
                str_temp += " OR department = " + "'" + department_list[int(each_ch)] + "'" 

            ### query        
        sql_string = "SELECT 1 id, COUNT(id) as coun, rank_number \
                    FROM data_WorkInfo WHERE" + str_temp + " GROUP BY rank_number"
        # print(sql_string)
        query =  WorkInfo.objects.raw(sql_string)
        temp_dict['rank'] = [['ค.ศ.', 'จำนวน']]
        for p in query:
            temp_dict['rank'].append([p.rank_number, p.coun])
            # print("----------")



        ######   EDUCATION
        education_query_str = [
            [" acronym_bachelor<>'' AND acronym_master='' AND acronym_phd='' ","ปริญญาตรี"],
            [" acronym_bachelor<>'' AND acronym_master<>'' AND acronym_phd='' ","ปริญญาโท"],
            [" acronym_bachelor<>'' AND acronym_master<>'' AND acronym_phd<>'' ","ปริญญาเอก"],

         ]

        temp_dict['education'] = [['ปริญญา', 'คน']]
        for each in education_query_str:
    
            sql_string = "SELECT 1 id, COUNT(acronym_bachelor) as coun \
                            FROM data_Education as e INNER JOIN data_WorkInfo as w \
                            ON e.user_id = w.user_id WHERE ("+ each[0] + ") AND (" + str_temp + ")"
            # print(sql_string)
            query2 =  Education.objects.raw(sql_string)[0]
            
            temp_dict['education'].append([each[1], query2.coun])
        
    else:
        str_temp = ""

    json_data = json.dumps(temp_dict)
    return render(request, 'reports/graph.html',{'json_data':json_data}  )

def statistics(request):

    rank_list = []
    rank_all = 0
    number_all_teacher = 0

    education_list = []
    education_all = 0

    checkbox_list = []

    department_list = ['ฝ่ายบริหาร',
                       'กลุ่มสาระการเรียนรู้วิทยาศาสตร์',
                       'กลุ่มสาระการเรียนรู้คณิตศาสตร์',
                       'กลุ่มสาระการเรียนรู้ศิลปะ',
                       'กลุ่มสาระการเรียนรู้ภาษาไทย',
                       'กลุ่มสาระการเรียนรู้ภาษาต่างประเทศ',
                       'กลุ่มสาระการเรียนรู้สังคมศึกษา ศาสนา และวัฒนธรรม',
                       'กลุ่มสาระการเรียนรู้การงานอาชีพและเทคโนโลยี',
                       'กลุ่มสาระการเรียนรู้สุขศึกษาและพลศึกษา',
                       'กิจกรรมพัฒนาผู้เรียน'
                       ]

    for i,each_name in enumerate(department_list):
        checkbox_list.append([i,'',each_name])

    checklist = request.POST.getlist('checks[]')

    if request.method == 'POST' and len(checklist) > 0 :        

        ###### CONCAT STRING
        
        str_temp = ""   
        for ind, each_ch in enumerate(checklist):
            checkbox_list[int(each_ch)][1] = "checked"
            if ind == 0:
                str_temp += " department = " + "'" + department_list[int(each_ch)] + "'" 
            else:
                str_temp += " OR department = " + "'" + department_list[int(each_ch)] + "'" 


        ######  RANK    
       
            ### query each number       
        sql_string = "SELECT 1 id, COUNT(id) as coun, rank_number \
                    FROM data_WorkInfo WHERE" + str_temp + " GROUP BY rank_number ORDER BY rank_number"        
        query =  WorkInfo.objects.raw(sql_string)
        rank_list.append(['ค.ศ.', 'จำนวน'])       
        for p in query:
            rank_list.append([p.rank_number, p.coun])
            rank_all += p.coun

            #### all user
        sql_string3 = "SELECT 1 id, COUNT(id) as coun \
                    FROM data_WorkInfo "
        query3 =  WorkInfo.objects.raw(sql_string3)       
        for p in query3:
            number_all_teacher = p.coun


        ######   EDUCATION
        education_query_str = [
            [" acronym_bachelor='' AND acronym_master='' AND acronym_phd='' ","ไม่กรอกวุฒิการศึกษา"],
            [" acronym_bachelor<>'' AND acronym_master='' AND acronym_phd='' ","ปริญญาตรี"],
            [" acronym_bachelor<>'' AND acronym_master<>'' AND acronym_phd='' ","ปริญญาโท"],
            [" acronym_bachelor<>'' AND acronym_master<>'' AND acronym_phd<>'' ","ปริญญาเอก"],

         ]

        education_list = [['ปริญญา', 'คน']]
        for each in education_query_str:
    
            sql_string = "SELECT 1 id, COUNT(acronym_bachelor) as coun \
                            FROM data_Education as e INNER JOIN data_WorkInfo as w \
                            ON e.user_id = w.user_id WHERE ("+ each[0] + ") AND (" + str_temp + ")"
            # print(sql_string)
            query2 =  Education.objects.raw(sql_string)[0]            
            education_list.append([each[1], query2.coun])
            education_all += query2.coun

    return render(request, 'reports/statistics.html',{
                        'rank_list':rank_list ,
                        'rank_all':rank_all,
                        'number_all_teacher':number_all_teacher,
                        'education_list':education_list,
                        'education_all':education_all,
                        'checkbox_list':checkbox_list })

def csv_export(request):

    if request.method == 'POST' and len(request.POST.getlist('checks[]')) > 0 :
        checklist = request.POST.getlist('checks[]')
        check_insignia = False
        if 'insignia' in checklist:
            check_insignia = True 
            checklist.remove('insignia')

        str_name = ""

        for i in checklist[:-1]:
            str_name += i+", "
        str_name += checklist[-1]
        print("-------------------"+str_name)

        sql_string = "SELECT p.id, p.user_id, " + str_name +  \
                " FROM data_PersonalInfo as p   \
                  INNER JOIN data_Address as a  \
                    ON p.user_id = a.user_id   \
                  INNER JOIN data_WorkInfo as w \
                    ON a.user_id = w.user_id   \
                  INNER JOIN data_Education as e  \
                    ON w.user_id = e.user_id "


        query2 =  WorkInfo.objects.raw(sql_string)

        # file_type = request.POST.['file_type']
        # if file_type == 'csv':
        #     return export_csv_file()
        # else file_type == 'xls':
        #     return export_xls_file()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="pwcrew_export.csv"'
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)


        ########################
        ####  write header  ####
        ########################
        first_row = check_group(checklist)
        second_row = check_subgroup(checklist)        
        verbose_name_dict = get_verbose_name_dict()
        list_title = []
        for i in checklist:
            print(verbose_name_dict[i])
            list_title.append(verbose_name_dict[i])
        if check_insignia:
            first_row.append('เครื่องราชอิสริยาภรณ์')
            second_row.append('')
            checklist.append('ชั้นและวันที่')

        titleName_list = ['title','spouse_title','father_title','mother_title']
        dateName_list = ['birth_date','start_service_date','end_service_date','start_PW_date']

        ## for insert blank for thai title
        temp = 1
        for index,value in enumerate(checklist):
            if value in titleName_list : 
                print(index)
                first_row.insert(index+temp,' ')
                second_row.insert(index+temp,' ')
                list_title.insert(index+temp,' ')
                temp += 1         
        writer.writerow(first_row)
        writer.writerow(second_row) 
        writer.writerow(list_title)        

        #####################
        #### write data  ####
        #####################
        for i in query2:
            # import pdb; pdb.set_trace()
            result_list = []            
            checklist2 = checklist
            if check_insignia:
                checklist2 = checklist[:-1]
            for j in checklist2:
                value = getattr(i, j)

                ### for extract title Eng and Thai                
                if j in titleName_list :                       
                    splitStr = value.split("(")
                    if len(splitStr) > 1:                        
                        engTitle = splitStr[0]
                        thaiTitle = splitStr[1][:-1]                              
                    else:
                        engTitle = ''
                        thaiTitle = ''

                    result_list.append(engTitle)   
                    result_list.append(thaiTitle) 

                elif j in dateName_list:
                    result_list.append( AD_date_to_BD_str(value) )
                else:
                    result_list.append(value )

            if check_insignia:
                result_list.append( get_all_insignia(i) )         
            
            writer.writerow(result_list)

        return response
    else:
        result_dict = get_all_field()
        return render(request,'reports/csv_export.html', result_dict)


model_dict = {
                    'PersonalInfo':PersonalInfo,
                    'Address':Address,
                    'WorkInfo':WorkInfo,
                    'Insignia':Insignia,
                    'Education':Education 
                }

########## Reports
def check_group(checklist):
    set_of_field = get_all_field()
    group = []
    group.append(["ข้อมูลส่วนตัว", column(set_of_field['PersonalInfo'],0) ])
    group.append(["ข้อมูลที่อยู่", column(set_of_field['Address'],0) ])
    group.append(["ข้อมูลการทำงาน", column(set_of_field['WorkInfo'],0) ])
    group.append(["ข้อมูลเครื่องราชอิสริยาภรณ์", column(set_of_field['Insignia'],0) ])
    group.append(["ข้อมูลการศึกษา", column(set_of_field['Education'],0) ])
    return add_head(group, checklist)   

def check_subgroup(checklist):
    group = [
        [
            "ชื่อคู่สมรส",
            ['spouse_title', 'firstname_spouse_thai', 'lastname_spouse_thai', 'firstname_spouse_eng', 'lastname_spouse_eng']
        ],
        [
            "ชื่อบิดา",
            ['father_title', 'firstname_father_thai', 'lastname_father_thai', 'firstname_father_eng', 'lastname_father_eng']
        ],
        [
            "ชื่อมารดา",
            ['mother_title', 'firstname_mother_thai', 'lastname_mother_thai', 'firstname_mother_eng', 'lastname_mother_eng']
        ],
        [
            "ที่อยู่ตามทำเบียนบ้าน",
            [
                'number_regis',
                'village_no_regis',
                'village_name_regis',
                'lane_regis',
                'road_regis',
                'sub_district_regis',
                'district_regis',
                'province_regis',
                'postal_code_regis',
                'smartphone_number_regis',
                'phone_number_regis',
            ]
        ],
        [
            "ที่อยู่ปัจจุบัน",
            [
                'number',
                'village_no',
                'village_name',
                'lane',
                'road',
                'sub_district',
                'district',
                'province',
                'postal_code',
                'smartphone_number',
                'phone_number',
            ]
        ],
        [
            "ปริญญาตรี",
            [
                'acronym_bachelor',
                'major_field_bachelor',
                'minor_field_bachelor',
                'university_bachelor',
                'start_year_bachelor',
                'end_year_bachelor',             
            ]
        ],
        [
            "ปริญญาโท",
            [
                'acronym_master',
                'major_field_master',
                'minor_field_master',
                'university_master',
                'start_year_master',
                'end_year_master',      
            ]
        ],
        [
            "ปริญญาเอก",
            [
                'acronym_phD',
                'major_field_phD',
                'minor_field_phD',
                'university_phD',
                'start_year_phD',
                'end_year_phD',      
            ]
        ],

    ]
    return add_head(group, checklist)

def add_head(group, checklist):
    first_row = []
    cur_group = -1
   
    for st in checklist:
        position = -1            
        for ind, i in enumerate(group):
            # print(i[1])
            if st in i[1]:   
                # print(st+" "+)           
                position = ind
                break

        if position <= cur_group:
            first_row.append('')
        elif position > cur_group:
            cur_group = position
            # print("--------"+str(position))
            # print(st)
            # print(group[cur_group][1])
            first_row.append(group[cur_group][0])
    return first_row

def get_all_insignia(obj):
    all_insignia = Insignia.objects.filter( user=obj.user_id )
    str_name = ""
    for i in all_insignia:
        str_name += "ชั้น " + str(i.class1) +" วันที่ " + AD_date_to_BD_str(i.date1) +"\n"
    return str_name

def get_all_field():   
    result_dict = {}
    for i_key, i_model in model_dict.items():
        result_dict[i_key] = []
        for i in i_model._meta.get_fields():
            if i.name.lower() != i.verbose_name.lower():
                result_dict[i_key].append([i.name, i.verbose_name])
                # if i_key == 'WorkInfo':
                    # print(i.name)

    return result_dict

def get_verbose_name_dict():
    result_dict = {}    
    for i_key, i_model in model_dict.items():
        for i in i_model._meta.get_fields():
            if i.name.lower() != i.verbose_name.lower():
                result_dict[i.name] = i.verbose_name

    return result_dict

def column(matrix, i):
    return [row[i] for row in matrix]

##### CSV
def export_csv_file(data):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)

    for i in data:
        writer.writerow(i)    
    return response
##### XLS