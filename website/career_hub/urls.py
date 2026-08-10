from django.urls import path
from . import views

app_name = 'career_hub'

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('cv/', views.cv, name='cv'),
    path('projects/', views.projects, name='projects'),
    path('personalstatement/', views.personalstatement, name='personalstatement'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('skills/', views.skills, name='skills'),
]