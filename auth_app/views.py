
from django.shortcuts import render

def login_user(request):
    return render(request,'auth_app/login.html')

def register_user(request):
    return render(request,'auth_app/register.html')

def change_password(request):
    return render(request,'auth_app/recover-password.html')
