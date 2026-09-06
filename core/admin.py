from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["full_name", "user", "phone", "position", "department"]
    search_fields = ["full_name", "user__username", "user__email"]
    list_filter = ["department", "position"]
    raw_id_fields = ["user"]
    
