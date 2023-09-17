from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group , User
from modeltranslation.admin import TranslationAdmin
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from reportlab.pdfgen import canvas




@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('name',)}
    group_fieldsets = True

    def has_view_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ProviderServices)
class ProviderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'name': ('name',)}
    list_display = ( 'name','provider',)
    group_fieldsets = True

    def has_view_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_vendor:
           return False
        else:
            return True
        
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }