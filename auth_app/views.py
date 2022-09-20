from audioop import reverse
from django.shortcuts import render,redirect
from django.contrib import messages 
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .utils import generate_token
from helpers.decoratoz import block_authed_user
# from .send_mail import send_activation_email


def register_user(request):
    if request.method =="POST":
        context={'has_error':False,'data':request.POST}
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if len(password)<6 or password!= password2:
            messages.add_message(request,messages.ERROR, "Password error")
            context["has_error"] = True

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.add_message(request,messages.ERROR, "Username/email is taken")
            context["has_error"] = True
            return render(request,'auth_app/register.html',context, status=409)

        if context["has_error"]:
            return render(request,'auth_app/register.html',context)

        user = User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.save()

        # send_activation_email(user,request)


        messages.add_message(request,messages.SUCCESS, f"Account created for {email}, Check inbox for activation link")
        return redirect('login')


    return render(request,'auth_app/register.html')

def login_user(request):
    if request.method =="POST":
        context={'has_error':False,'data':request.POST}
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request,username=email,password=password)
        # if not user.is_email_verified:
        #     messages.add_message(request,messages.ERROR, "Email not verified")
        #     return render(request,'auth_app/login.html',context)

        if not user:
            messages.add_message(request,messages.ERROR, "Wrong User Credentials")
            return render(request,'auth_app/login.html',context)
        
        login(request,user)
        messages.add_message(request,messages.SUCCESS, f"Welcome {user.username}")
        return redirect(reverse('home'))

    return render(request,'auth_app/login.html')

def logout_user(request):
    print('logged out')
    logout(request)
    messages.add_message(request,messages.SUCCESS, "Logged out successfully")
    return redirect(reverse('login'))


def change_password(request):
    return render(request,'auth_app/recover-password.html')

def activate_user(request,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)


    except Exception as e:
        user=None

    if user and generate_token.check_token(user,token):
        user.is_email_verified=True
        user.save()

        messages.add_message(request,messages.SUCCESS, f"Activated {user.username} account")
        return redirect(reverse('login'))

    return render(request,'auth_app/activate_failed.html',{'user':user})
