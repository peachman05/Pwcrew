from django.shortcuts import render
import json
import csv
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect ,get_object_or_404
from data.models import *
from django.contrib import messages

def home(request):
    list_obj = NewsInHome2.objects.all()

    if list_obj.count() > 0:
        modelObj = NewsInHome2.objects.all()[0]
        news = modelObj.news
    else:
        obj = NewsInHome2(news="")
        obj.save()
        news = ""
    return  render(request, 'home.html', {'news':news} )

def edit_home(request):
    try: # edit
        print("edit")
        list_obj = NewsInHome2.objects.all()
        modelObj = list_obj[0]
        form = NewsInHome2Form(request.POST or None, instance=modelObj)
        print(modelObj)
        isCreate = False
    except NewsInHome2.DoesNotExist: # create
        print("create")
        form = NewsInHome2Form()
        isCreate = True


    if request.method == 'POST' :
        if isCreate:
            form = NewsInHome2Form(request.POSTS)

        if form.is_valid():
            messages.success(request, 'ดำเนินการสำเร็จ!!')
            form.save()
            return redirect('home')

        else:
            messages.error(request, 'โปรดแก้ข้อผิดพลาดด้านล่างก่อน')
        
    return  render(request, 'edit_home.html', {'form':form} )
