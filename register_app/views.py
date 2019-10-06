from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

## change pass word
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from data.models import *

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return render(request, 'home.html')
            messages.success(request, 'ดำเนินการสำเร็จ!!')

            p = PersonalInfo(user=user)
            p.save()

            a = Address(user=user)
            a.save()

            w = WorkInfo(user=user)
            w.save()

            # i = Insignia(user=user)
            # i.save()

            e = Education(user=user)
            e.save()

            

            return redirect('data:list_teacher')
        else:
            messages.error(request, 'โปรดแก้ข้อผิดพลาดด้านล่างก่อน')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'ดำเนินการสำเร็จ!!')
            return redirect('home')
        else:
            messages.error(request, 'โปรดแก้ข้อผิดพลาดด้านล่างก่อน')
    else:
        form = PasswordChangeForm(request.user)
        print(form)
    return render(request, 'change_password.html', {
        'form': form
    })