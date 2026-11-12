from django.contrib import admin
from .models import Tag, CareerHub, Project

# Register your models here.
admin.site.register(Tag)
admin.site.register(CareerHub)
admin.site.register(Project)