from django.shortcuts import render

def home(request):
    return render(request, 'career_hub/home.html')

def cv(request):
    return render(request, 'career_hub/cv.html')

def projects(request):
    return render(request, 'career_hub/projects.html')

def about(request):
    return render(request, 'career_hub/about.html')