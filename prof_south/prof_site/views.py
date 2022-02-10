from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('prof_site/index.html')
    return HttpResponse(template.render())

def news(request):
    return HttpResponse('"Тут будут профсоюзные новости"')

def contacts(request):
    template = loader.get_template('prof_site/contacts.html')
    return HttpResponse(template.render())

def documents(request):
    return HttpResponse('"Тут будут правовые документы Профсоюза"')

def regions(request,):
    template = loader.get_template('prof_site/regions.html')
    return HttpResponse(template.render())