from django.shortcuts import render, redirect

# Create your views here.

def home_f(request):
    return render(request, 'index.html')


def transcribe_f(request):
    return render(request, 'about.html')
