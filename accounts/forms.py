from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class LoginForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Phone", "class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )


class SignUpForm(UserCreationForm):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Phone", "class": "form-control"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        )
    )
    

    class Meta:
        model = User
        fields = ("phone", "email", "password1", "password2")
