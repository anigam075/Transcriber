from django.shortcuts import render, redirect
from .models import User_s
# from django.contrib.auth import login, authenticate
from .auth import authenticate, login, logout, get_user

# Create your views here.

def home_f(request):
    return render(request, 'index.html')

def transcribe_f(request):
    return render(request, 'about1.html')


def category_f(request):
    return render(request, 'category1.html')

def work_f(request):
    return render(request, 'work1.html')

def login_f(request):
    if request.method == 'POST':
        #return all the emails and password present in the database
        # emails = User_s.objects.values_list('email', flat=True)
        # passwords = User_s.objects.values_list('password', flat=True)
        # for email, password in zip(emails, passwords):
        #     print(email, password)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            print('user ------- ', user)
            return redirect('/') 
    return render(request, 'login1.html')

def logout_f(request):
    print('before logout ------ ',get_user(request))
    logout(request)
    print('after logout ------ ',get_user(request))
    return redirect('/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        user = User_s.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            password = password)
        user.save()
        print('registered')
        return redirect('login')
    return render(request, 'register1.html')
