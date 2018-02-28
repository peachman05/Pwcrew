from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from datetime import date
from django.core.files.storage import FileSystemStorage
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib import messages

from .models import *
# Create your views here.


def getForm(request,modelInput,modelFormInput,path,user_id_input,dict_send):

    if user_id_input == None:
        userInput = request.user
    elif request.user.is_staff:
        userInput = get_object_or_404(User, pk=user_id_input)

    # print(userInput.username)

    if request.user.is_authenticated:
        try: # edit
            modelObj = modelInput.objects.get(user=userInput.id)
            
            if path == "work_info" :
                personInfoObj = PersonalInfo.objects.get(user=userInput.id)
                birthDate = personInfoObj.birth_date
                if birthDate != None:
                    modelObj = modelInput.objects.get(user=userInput.id)
                    new_date = date(30,9,30)
                    if birthDate.month < 10:
                        new_date = date(birthDate.year + 60 ,9,30)
                    else:
                        new_date = date(birthDate.year + 61 ,9,30)

                    modelObj.end_service_date = new_date

                print( type(birthDate))
                print( str(modelObj.end_service_date.year) +" hhhh")

            if path == "personal_info" : 
                form = modelFormInput(request.POST or None,request.FILES or None , instance=modelObj)
            else:          
                form = modelFormInput(request.POST or None, instance=modelObj)
            isCreate = False
        except modelInput.DoesNotExist: # create
            print("create")
            form = modelFormInput()
            isCreate = True

        if request.method == 'POST' :
            print("in")
            if isCreate:
                form = modelFormInput(request.POST, request.FILES)
                print("ddd-")
                
                
            if form.is_valid():
                recipe = form.save(commit=False)
                recipe.user = userInput
                if path == "personal_info":                    
                    recipe.card_number = userInput.username

                    # if request.FILES["myfile"]:
                    #     myfile = request.FILES['myfile']
                    #     fs = FileSystemStorage()
                    #     filename = fs.save(myfile.name, myfile)
                    #     print(myfile.name+" dddd")
                    #     uploaded_file_url = fs.url(filename)
                    
                recipe.save()
                messages.success(request, 'ดำเนินการสำเร็จ!!')
                if request.user.is_staff:                    
                    return redirect('data:list_teacher')
                else:
                    return redirect('home')
                    # render(request,'data/'+path+'.html')
            else:
                messages.error(request, 'โปรดแก้ข้อผิดพลาดด้านล่างก่อน')

        dict_send['form'] = form
        # print(form)

        # for given name
        i = 0
        dict_send['form_tuple'] = []        
        for field in form:
            if len(dict_send['name_list']) > 0 :
                dict_send['form_tuple'].append( (dict_send['name_list'][i] , field) )
                print(field.id_for_label )
            i += 1

        return render(request,'data/'+path+'.html', dict_send)
    else:
        return redirect('login')

# def checkUser(request,modelInput,modelFormInput,path,user_id_input):
    if user_id_input == None:
        return getForm(request,modelInput,modelFormInput,path,request.user)
    elif request.user.is_staff:
        userObj = get_object_or_404(User, pk=user_id_input)
        return getForm(request,modelInput,modelFormInput,path,userObj)

def personal_info(request,user_id_input=None):
    dict_send = {'title':'Personal Information'}
    dict_send['name_list'] = [
        "คำนำหน้าชื่อ",
        "ชื่อจริง(ไทย)","นามสกุล(ไทย)",
        "ชื่อจริง(อังกฤษ)","นามสกุล(อังกฤษ)",
        "เลขประจำตัวประชาชน","ศาสนา",
        "หมู่โลหิต","วัน/เดือน/ปี เกิด",
        "Email","สภาณภาพ",
        "ภูมิลำเนาเดิมจังหวัด",
        "ชื่อจริงคู่สมรส(ไทย)","นามสกุลคู่สมรส(ไทย)",
        "ชื่อจริงคู่สมรส(อังกฤษ)","นามสกุลคู่สมรส(อังกฤษ)",
        "ชื่อจริงบิดา(ไทย)","นามสกุลบิดา(ไทย)",
        "ชื่อจริงบิดา(อังกฤษ)","นามสกุลบิดา(อังกฤษ)",
        "ชื่อจริงมารดา(ไทย)","นามสกุลมารดา(ไทย)",
        "ชื่อจริงมารดา(อังกฤษ)","นามสกุลมารดา(อังกฤษ)",
        "ชื่อจริงมารดา(อังกฤษ)","นามสกุลมารดา(อังกฤษ)",
        "ชื่อจริงมารดา(อังกฤษ)","นามสกุลมารดา(อังกฤษ)",
        "ชื่อจริงมารดา(อังกฤษ)","นามสกุลมารดา(อังกฤษ)",
    ]

    print(request.POST)
    print(request.FILES)
    return getForm(request,PersonalInfo,PersonalInfoForm,'personal_info',user_id_input,dict_send)

def address(request,user_id_input=None):
    dict_send = {'title':'Address'}
    dict_send['name_list'] = [
        "เลขที่",
        "หมู่",
        "หมู่บ้าน",
        "ซอย",
        "ถนน",
        "ตำบล",
        "อำเภอ",
        "จังหวัด",
        "รหัสไปรษณีย์",
        "เบอร์โทรศัพท์มือถือ",
        "เบอร์โทรศัพท์บ้าน",

        "เลขที่",
        "หมู่",
        "หมู่บ้าน",
        "ซอย",
        "ถนน",
        "ตำบล",
        "อำเภอ",
        "จังหวัด",
        "รหัสไปรษณีย์",
        "เบอร์โทรศัพท์มือถือ",
        "เบอร์โทรศัพท์บ้าน",

    ]
    return getForm(request,Address,AddressForm,'address',user_id_input,dict_send)

def work_info(request,user_id_input=None):
    dict_send = {'title':'Work Infomation'}
    dict_send['name_list'] = []
    return getForm(request,WorkInfo,WorkInfoForm,'work_info',user_id_input,dict_send)

def education(request,user_id_input=None):
    dict_send = {'title':'Education'}
    dict_send['name_list'] = [
        "<b>อักษรย่อ</b>",
        "<b>สาขาวิชาเอก</b>",
        "<b>สาขาวิชาโท</b>",
        "<b>สถาบัน</b>",
        "<b>ปีที่เริ่มศึกษา</b> <br>(ตัวอย่าง 30/12/2501)",
        "<b>ปีที่สำเร็จการศึกษา</b> <br>(ตัวอย่าง 30/12/2501)",

        "<b>อักษรย่อ</b>",
        "<b>สาขาวิชาเอก</b>",
        "<b>สาขาวิชาโท</b>",
        "<b>สถาบัน</b>",
        "<b>ปีที่เริ่มศึกษา</b> <br>(ตัวอย่าง 30/12/2501)",
        "<b>ปีที่สำเร็จการศึกษา</b> <br>(ตัวอย่าง 30/12/2501)",

        "<b>อักษรย่อ</b>",
        "<b>สาขาวิชาเอก</b>",
        "<b>สาขาวิชาโท</b>",
        "<b>สถาบัน</b>",
        "<b>ปีที่เริ่มศึกษา</b> <br>(ตัวอย่าง 30/12/2501)",
        "<b>ปีที่สำเร็จการศึกษา</b> <br>(ตัวอย่าง 30/12/2501)",

    ]

    return getForm(request,Education,EducationForm,'education',user_id_input, dict_send)



def list_teacher(request):
    teacher_obj_list = User.objects.filter(is_staff=False).order_by('username')  #[:5]
    # temp =  User.objects.select_related('personal_info')
    # print(temp)
    new_list = []
    for entry in teacher_obj_list:
        print(type(entry))

        try: # edit
            personEntry = PersonalInfo.objects.get(user=entry)
            nameStr = personEntry.firstname_thai+" "+personEntry.lastname_thai
        except PersonalInfo.DoesNotExist: # create
            nameStr = "Unknown"

        new_list.append((nameStr,entry))

    return render(request,'data/list_teacher.html', {'teacher_obj_list':new_list})


def delete_teacher(request,user_id_input=None):
    if request.user.is_staff:        
        if user_id_input != None:
            instance = User.objects.get(id=user_id_input)
            instance.delete()
            messages.success(request, 'ดำเนินการสำเร็จ!!')
    return redirect('data:list_teacher')


def insignia(request,user_id_input=None):
    dict_send = {'title':'Insignia'}
    dict_send['name_list'] = []

    if user_id_input == None:
        userInput = request.user
    elif request.user.is_staff:
        userInput = get_object_or_404(User, pk=user_id_input)

    insignia_list = Insignia.objects.filter(user=userInput.id)
    return render(request,'data/insignia.html', {'insignia_list':insignia_list, 'user_id_input':user_id_input})

def edit_insignia(request,insignia_id_input):    

    insignia_object = get_object_or_404(Insignia, pk=insignia_id_input)
    form = InsigniaForm(request.POST or None, instance=insignia_object)

    if request.method == 'POST' :
        id_user = insignia_object.user.id
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = get_object_or_404(User, pk=id_user)
            recipe.save()
            messages.success(request, 'ดำเนินการสำเร็จ!!')
            if request.user.is_staff:
                return HttpResponseRedirect(reverse('data:insignia') + str(id_user) )
            else:
                return redirect('data:insignia')
        else:
            messages.error(request, 'โปรดแก้ข้อผิดพลาดด้านล่างก่อน')
    print(form)
    return render(request,'data/edit_insignia.html', {'form':form})

def delete_insignia(request,insignia_id_input):        
    # if request.user.is_staff:        
    if insignia_id_input != None:
        insignia_object = get_object_or_404(Insignia, pk=insignia_id_input)
        id_user = insignia_object.user.id
        insignia_object.delete()
        messages.success(request, 'ดำเนินการสำเร็จ!!')

        if request.user.is_staff:
            return HttpResponseRedirect(reverse('data:insignia') + str(id_user) )
        else:
            return redirect('data:insignia')
    return redirect('home')

def add_insignia(request,user_id_input=None):

    if user_id_input == None:
        userInput = request.user
    elif request.user.is_staff:
        userInput = get_object_or_404(User, pk=user_id_input)
        
    if request.method == 'POST' :
        form = InsigniaForm(request.POST)
        if form.is_valid():            
            recipe = form.save(commit=False)
            recipe.user = userInput
            recipe.save()
            messages.success(request, 'ดำเนินการสำเร็จ!!')
            if request.user.is_staff:
                return HttpResponseRedirect(reverse('data:insignia') + str(userInput.id) )
            else:
                return redirect('data:insignia')
        else:
            messages.error(request, 'โปรดแก้ข้อผิดพลาดด้านล่างก่อน')
    else:        
        form = InsigniaForm()

    return render(request, 'data/add_insignia.html', {'form': form})

    # return getForm(request,Insignia,InsigniaForm,'insignia',user_id_input,dict_send)


def reset_password(request,user_id_input):

    if request.method == 'POST' :
        password = request.POST.get('password', '')
        user = get_object_or_404(User, pk=user_id_input)
        user.set_password(password)
        user.save()
        messages.success(request, 'ดำเนินการสำเร็จ!!')
        return redirect('data:list_teacher')

    return render(request, 'data/reset_password.html' )


def change_username(request,user_id_input):

    if request.method == 'POST' :
        new_username = request.POST.get('new_username', '')        
        user = get_object_or_404(User, pk=user_id_input)
        user.username = new_username
        user.save()
        messages.success(request, 'ดำเนินการสำเร็จ!!')
        return redirect('data:list_teacher')

    return render(request, 'data/change_username.html' )