from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):
    return render (request,'register.html')

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if password == confirm_password:
        if User.objects.filter(username=username).exists():
            # print('username taken')
            messages.info(request,'Username Taken')
            return redirect('register')
        elif  User.objects.filter(email=email).exists():
            # print('email taken')
            messages.info(request,'Email Taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username = username, first_name = first_name, last_name = last_name, password = password,email = email)
            user.save()
            # print("user created")
            # messages.info(request,'User created')
            return redirect('login')
           
    else:
        # print('password do not match ')
        messages.info(request,'password do not match')
        return redirect('register')


def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'username or password do not match')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')