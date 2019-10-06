from django.shortcuts import render
from django.shortcuts import render, redirect ,get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from datetime import date
from django.core.files.storage import FileSystemStorage
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib import messages
from . import viewHelper

import datetime

from .models import *


personalInfo_nameList = [
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

address_nameList = [
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

education_nameList = [
        "<b>อักษรย่อ</b>",
        "<b>สาขาวิชาเอก</b>",
        "<b>สาขาวิชาโท</b>",
        "<b>สถาบัน</b>",
        "<b>ปีที่เริ่มศึกษา</b> <br>(ตัวอย่าง 2538)",
        "<b>ปีที่สำเร็จการศึกษา</b> <br>(ตัวอย่าง 2538)",

        "<b>อักษรย่อ</b>",
        "<b>สาขาวิชาเอก</b>",
        "<b>สาขาวิชาโท</b>",
        "<b>สถาบัน</b>",
        "<b>ปีที่เริ่มศึกษา</b> <br>(ตัวอย่าง 2538)",
        "<b>ปีที่สำเร็จการศึกษา</b> <br>(ตัวอย่าง 2538)",

        "<b>อักษรย่อ</b>",
        "<b>สาขาวิชาเอก</b>",
        "<b>สาขาวิชาโท</b>",
        "<b>สถาบัน</b>",
        "<b>ปีที่เริ่มศึกษา</b> <br>(ตัวอย่าง 2538)",
        "<b>ปีที่สำเร็จการศึกษา</b> <br>(ตัวอย่าง 2538)",

    ]

def getForm(ip_p): # ip_p is input_pack

    #### if user not authen, just redirect them
    if not ip_p['request'].user.is_authenticated:
        return redirect('login')
    ## userInput is userobj of this form
    # There are 2 possible events, 1. call from that user(userID==None) 2. call from admin(give userID)
    if ip_p['user_id_input'] == None:
        userInput = ip_p['request'].user
    elif ip_p['request'].user.is_staff:
        userInput = get_object_or_404(User, pk=ip_p['user_id_input'])

    ### get modelObj
    # try: 
    modelObj = ip_p['modelInput'].objects.get(user=userInput.id)
    # except ip_p['modelInput'].DoesNotExist: # create
    #     modelObj = None    

    ## if modelObj is None, it will create new instance in database
    ## if modelObj is not None, it will update that instance in database
    form = ip_p['modelFormInput'](ip_p['request'].POST.copy() or None,ip_p['request'].FILES or None , instance=modelObj)
    
    ## try to save if it POST method
    if ip_p['request'].method == 'POST' :
        # is_save, redirect_dest, form = viewHelper.tryToSave(ip_p, userInput, modelObj)
        is_save, redirect_dest = viewHelper.tryToSave(ip_p, userInput, form)
        if is_save:
            return redirect_dest
    else:
        form = viewHelper.fixDateinRegularForm(ip_p['path'], form)
    
    ## change date format and prepare new dict for sending to front-end
    new_dict_send = viewHelper.prepareToFront(ip_p, form, ip_p['dict_send'], modelObj)

    return render(ip_p['request'],'data/'+ ip_p['path'] +'.html', new_dict_send)


def personal_info(request,user_id_input=None):
    dict_send = {'title':'Personal Information'}
    dict_send['name_list'] = personalInfo_nameList 
    input_pack = viewHelper.packDataToDict(request,PersonalInfo,PersonalInfoForm,'personal_info',user_id_input,dict_send)
    return getForm(input_pack)

def address(request,user_id_input=None):
    dict_send = {'title':'Address'}
    dict_send['name_list'] = address_nameList
    input_pack = viewHelper.packDataToDict(request,Address,AddressForm,'address',user_id_input,dict_send)
    return getForm(input_pack)

def work_info(request,user_id_input=None):
    dict_send = {'title':'Work Infomation'}
    dict_send['name_list'] = []
    input_pack = viewHelper.packDataToDict(request,WorkInfo,WorkInfoForm,'work_info',user_id_input,dict_send)
    return getForm(input_pack)

def education(request,user_id_input=None):
    dict_send = {'title':'Education'}
    dict_send['name_list'] = education_nameList
    input_pack = viewHelper.packDataToDict(request,Education,EducationForm,'education',user_id_input, dict_send)
    return getForm(input_pack)

def list_teacher(request):
    teacher_obj_list = User.objects.filter(is_staff=False).order_by('username') #order_by('username')  #[:5]
    new_list = []
    for entry in teacher_obj_list:
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
    
    if request.method == 'POST' :
        id_user = insignia_object.user.id

        #  #### use this trick for changing some data after we get its form
        # changed_data = dict(request.POST)
        # for key in changed_data:
        #     changed_data[key] = changed_data[key][0]

        # import pdb; pdb.set_trace()
        # #### preprocess some data        
        # date_value = changed_data['date1']  
        # if date_value != '' :           
        #     changed_data['date1'] = viewHelper.BD_str_to_AD_str(date_value)

        form = InsigniaForm(request.POST.copy(), instance=insignia_object)
        form = viewHelper.fixDateinPostForm('insignia', form, toAC=True)
        # import pdb; pdb.set_trace()
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
            form = viewHelper.fixDateinPostForm('insignia', form, toAC=False)
    else:
        form = InsigniaForm(request.POST or None, instance=insignia_object)
        form = viewHelper.fixDateinRegularForm('insignia', form)
        
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
        form = InsigniaForm(request.POST.copy())
        form = viewHelper.fixDateinPostForm('insignia', form, toAC=True)
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