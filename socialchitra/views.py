from django.shortcuts import render


def home(request):
    return render(request,'index-6.html')

def services(request):
    return render(request,'services.html')

def about_us(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')
