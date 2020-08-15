from django.contrib import admin

from.models import Pet

@admin.register(Pet)
class petAdmin(admin.ModelAdmin):
    list_display = ['name','species','breed','age','sex']

