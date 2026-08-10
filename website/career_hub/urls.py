from django.urls import path
from . import views

app_name = 'career_hub'

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('cv/', views.cv, name='cv'),
    path('about/', views.about, name='about'),
]