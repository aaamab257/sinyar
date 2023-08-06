from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' , 'name' , 'is_admin')