from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import OnBoarding , OffersSlider

# Register your models here.
admin.site.register(OffersSlider)




@admin.register(OnBoarding)
class OnBoardingAdmin(TranslationAdmin):
    prepopulated_fields = {'title': ('title','desc')}
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







# @admin.register(OffersSlider)
# class OffersSliderAdmin(TranslationAdmin):
#     prepopulated_fields = {'title': ('title')}
#     group_fieldsets = True
#     class Media:
#         js = (
#             'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
#             'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
#             'modeltranslation/js/tabbed_translation_fields.js',
#         )
#         css = {
#             'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
#         }