from django.urls import path
from . import views

urlpatterns = [
    path('', views.dmoapp, name='dmoapp'),
    path('tunes/', views.tunes, name='tunes'),

]