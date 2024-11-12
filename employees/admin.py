from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display = ('name', 'position', 'dept', 'contact', 'employment_type', 'hired')
    search_fields = ('name', 'position', 'dept')