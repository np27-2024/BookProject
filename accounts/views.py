from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from accounts.models import  UserProfile, loginInfo

# Create your views here.


def register_user(request):
    if request.method == "POST":

        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This username already exists')  # this message gets printed to the web page
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This mail id already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save()
            return redirect('login')

        else:
            messages.info(request, 'This password is not matching')
            return redirect('register')

    return render(request, 'accounts/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('User_list_view')
        else:
            messages.info(request, 'Please provide valid credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')


def log_out(request):
    auth.logout(request)
    return redirect('login')


def home_page(request):
    return render(request, 'accounts/Home.html')



