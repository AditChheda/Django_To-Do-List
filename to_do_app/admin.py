from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *
# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("priority", "title", "description");