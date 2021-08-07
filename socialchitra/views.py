from django.shortcuts import render
from databases.models import Team,WhyUs,Service

def home(request):
    return render(request,'index-6.html')

def services(request):
    services = Service.objects.filter(hidden=False)
    return render(request,'services.html',{'services':list(services)})

def about_us(request):
    why_us = WhyUs.objects.filter(hidden=False).order_by('id')
    team = Team.objects.filter(hidden=False).order_by('id')
    return render(request,'about.html',{'why_us':list(why_us),'team':list(team)})

def contact(request):
    return render(request, 'contact.html')
