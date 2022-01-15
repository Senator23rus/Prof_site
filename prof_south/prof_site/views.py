from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('"Это будет главная страница Профсайта"')

def news(request):
    return HttpResponse('"Тут будут профсоюзные новости"')

def contacts(request):
    return HttpResponse('"Тут будут контакты аппарата Профсоюза"')

def documents(request):
    return HttpResponse('"Тут будут правовые документы Профсоюза"')

def filials(request, filial_name):
    return HttpResponse(f"Тут будет отсылка на филиалы</h1><p>{filial_name}</p>")