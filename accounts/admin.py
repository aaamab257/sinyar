from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.






@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        is_admin = request.user.is_admin
        if not is_admin:
           return False
        else:
            return True
        
    def has_change_permission(self, request, obj=None):
        is_admin = request.user.is_admin
        if not is_admin:
           return False
        else:
            return True
        
    def has_add_permission(self, request, obj=None):
        is_admin = request.user.is_admin
        if not is_admin:
           return False
        else:
            return True    

