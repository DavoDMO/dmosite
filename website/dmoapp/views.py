from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def dmoapp(request):
    template = loader.get_template('dmoapp/main.html')
    return HttpResponse(template.render())

def tunes(request):
    template = loader.get_template('dmoapp/tunes.html')
    return HttpResponse(template.render())