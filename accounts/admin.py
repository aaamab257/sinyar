from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import *

# Register your models here.


class UsersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"name": ("name",)}
    list_display = ("name", "email")
    search_fields = ("name", "email", "phone")
    list_filter = ("name", "email", "phone")
    fieldsets = (
        ('User Credentials', {'fields': ('phone', 'password' )}),
        ('Personal info', {'fields': ('name','email','date_of_birth' , 'fcm_token')}),
        ('Permissions', {'fields': ('is_admin', 'is_vendor', 'is_active' , 'is_superuser')}),
        
    )
    

    def has_add_permission(self, request):
        if request.user.is_admin:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_admin:
            if not request.user.is_vendor:
               return True
        else:
            return False
        
    def has_view_permission(self, request, obj=None):
        if request.user.is_vendor:
            return False
        else:
            return True


admin.site.register(User, UsersAdmin)
