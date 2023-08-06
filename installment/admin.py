from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(InstallMentsPlans)
class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('num_installments', 'interest')
    group_fieldsets = True
    


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ('plan', 'amount')
    group_fieldsets = True
    
    