from django import forms
from django.contrib import admin
from .models import Installment

class InstallmentAdminForm(forms.ModelForm):
    duration = forms.IntegerField()

    class Meta:
        model = Installment
        fields = '__all__'

class InstallmentAdmin(admin.ModelAdmin):
    form = InstallmentAdminForm

admin.site.register(Installment, InstallmentAdmin)