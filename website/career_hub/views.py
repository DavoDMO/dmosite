from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'career_hub/home.html')

def cv(request):
    return render(request, 'career_hub/cv.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'career_hub/projects.html', {'projects': projects})

def about(request):
    return render(request, 'career_hub/about.html')