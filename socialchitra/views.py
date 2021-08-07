from django.shortcuts import render
from databases.models import Team,WhyUs

def home(request):
    return render(request,'index-6.html')

def services(request):
    return render(request,'services.html')

def about_us(request):
    why_us = WhyUs.objects.all().order_by('id')
    return render(request,'about.html',{'why_us':list(why_us)})

def contact(request):
    return render(request, 'contact.html')
