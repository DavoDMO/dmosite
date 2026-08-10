from django.shortcuts import render

def home(request):
    return render(request, 'career_hub/home.html')

def portfolio(request):
    return render(request, 'career_hub/portfolio.html')

def cv(request):
    return render(request, 'career_hub/cv.html')

def projects(request):
    return render(request, 'career_hub/projects.html')

def personalstatement(request):
    return render(request, 'career_hub/personalstatement.html')

def education(request):
    return render(request, 'career_hub/education.html')

def experience(request):
    return render(request, 'career_hub/experience.html')

def skills(request):
    return render(request, 'career_hub/skills.html')
