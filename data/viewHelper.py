from datetime import datetime
from datetime import date
from .models import *
from django.contrib import messages
from django.shortcuts import redirect


def try_parsing_date(text):
    for fmt in ('%d-%m-%Y', '%d.%m.%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            ## format is not valid
            pass
    # raise ValueError('no valid date format found')
    return None

# use after get data and want to save it
def BD_str_to_AD_str(date_str): # change BD to AD as date(พ.ศ. -> ค.ศ.) d/m/Y(str) -> date
    # change BC year str to AC str
    d, m, y = date_str.split("/",2)
    AD_y = str(int(y) - 543 )
    AD_str = d+'/'+m+'/'+AD_y
    return AD_str

# use when you send data to show at front-end
def AD_date_to_BD_str(dateObj): # change AD to BD as string(ค.ศ. -> พ.ศ.) date -> d/m/Y (str)
    # import pdb; pdb.set_trace()
    if isinstance(dateObj, date):
        AD_str = dateObj.strftime('%d/%m/%Y') #  date to str
    else:
        AD_str = dateObj
    # change AC year str to BC str
    d, m, y = AD_str.split("/",2)
    BD_y = str(int(y) + 543 )
    BD_str = d+'/'+m+'/'+BD_y 
    
    return BD_str


def packDataToDict(request,modelInput,modelFormInput,path,user_id_input,dict_send):
    input_pack = {}
    input_pack['request'] = request
    input_pack['modelInput'] = modelInput
    input_pack['modelFormInput'] = modelFormInput
    input_pack['path'] = path
    input_pack['user_id_input'] = user_id_input
    input_pack['dict_send'] = dict_send
    return input_pack

def fixDateinPostForm(path, form, toAC=False):
   
    if toAC:
        ### because we cannot use '' != '' to check empty string. 
        ### So, just check that variable in if
        # is_null = ''
        trans_func = BD_str_to_AD_str
    else:
        # is_null = None
        trans_func = AD_date_to_BD_str

    #### preprocess some data
    if path == "personal_info":
        date_value = form.data['birth_date']  
        if date_value:  #  if it's None or '', it will get False         
            form.data['birth_date'] = trans_func(date_value)
    
    if path == "work_info":
        start_service_date = form.data['start_service_date']               
        if start_service_date:
            form.data['start_service_date'] = trans_func(start_service_date)
        # import pdb; pdb.set_trace()
        end_service_date = form.data['end_service_date']            
        if end_service_date:
            form.data['end_service_date'] = trans_func(end_service_date)
    
        start_PW_date = form.data['start_PW_date']              
        if start_PW_date:
            form.data['start_PW_date'] = trans_func(start_PW_date)  

    if path == "insignia":
        date_value = form.data['date1']  
        if date_value:           
            form.data['date1'] = trans_func(date_value)

    return form


def fixDateinRegularForm(path, form):
    is_null = None
    trans_func = AD_date_to_BD_str
    if path == "personal_info":
        date_value = form['birth_date'].value()  
        if date_value != is_null  :           
            form['birth_date'].initial = trans_func(date_value)

    if path == "work_info":
        start_service_date = form['start_service_date'].value()                
        if start_service_date != is_null :
            form['start_service_date'].initial = trans_func(start_service_date)
        
        end_service_date = form['end_service_date'].value()             
        if end_service_date != is_null :
            form['end_service_date'].initial = trans_func(end_service_date)
    
        start_PW_date = form['start_PW_date'].value()               
        if start_PW_date != is_null :
            form['start_PW_date'].initial = trans_func(start_PW_date)  
    
    if path == "insignia":
        date_value = form['date1'].value()                
        if date_value != is_null :
            form['date1'].initial = trans_func(date_value)


    return form

def tryToSave(ip_p, userInput, form):

    form = fixDateinPostForm(ip_p['path'], form,toAC=True)
   
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.user = userInput 
        

        if ip_p['path'] == "personal_info":                    
            recipe.card_number = userInput.username
            birthDate = try_parsing_date(form.data['birth_date'])
            # birthDate = form.data['birth_date']
            if birthDate:
                workInfoObj = WorkInfo.objects.get(user=userInput.id)
                if birthDate.month < 10:
                    new_date = date(birthDate.year + 60 ,9,30)
                else:
                    new_date = date(birthDate.year + 61 ,9,30)
                workInfoObj.end_service_date = new_date
                workInfoObj.save()

        recipe.save()

        ## show message in base.html
        messages.success(ip_p['request'], 'ดำเนินการสำเร็จ!!')        
        if ip_p['request'].user.is_staff:                    
            redirect_dest = redirect('data:list_teacher')
        else:
            redirect_dest = redirect('home')        
        is_save = True             
    else:
        messages.error(ip_p['request'], 'โปรดแก้ข้อผิดพลาดด้านล่างก่อน')
        form = fixDateinPostForm(ip_p['path'], form,toAC=False)

        is_save = False
        redirect_dest = None
    return is_save, redirect_dest



def prepareToFront(ip_p, form, dict_send, modelObj=None):

    # set form data and send to front-end
    # import pdb; pdb.set_trace()
    # form = fixDateinForm(ip_p, form,toAC=False)
    dict_send['form'] = form

    ## change datetime when open the page for edit Y-m-d --> d/m/Y (just for good looking)    
    if ip_p['path'] == "personal_info" :        
        dict_send['path_picture'] = "/media/" + str(modelObj.image)      
        
    
    #     date_value = form['birth_date'].value() 
    #     if date_value != None :
    #        form['birth_date'].initial = AD_date_to_BD_str(date_value)
    
    # elif path == "work_info" :
    #     start_service_date = form['start_service_date'].value()                
    #     if start_service_date != None :
    #         form['start_service_date'].initial = AD_date_to_BD_str(start_service_date)
        
    #     end_service_date = form['end_service_date'].value()               
    #     if end_service_date != None :
    #         form['end_service_date'].initial = AD_date_to_BD_str(end_service_date)
    
    #     start_PW_date = form['start_PW_date'].value()                
    #     if start_PW_date != None :
    #         form['start_PW_date'].initial = AD_date_to_BD_str(start_PW_date)
    
    ### for given name
    dict_send['form_tuple'] = []        
    for i,field in enumerate(form):
        if len(dict_send['name_list']) > 0 :
            dict_send['form_tuple'].append( (dict_send['name_list'][i] , field) )

    return dict_send
