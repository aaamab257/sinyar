from django.shortcuts import render, redirect
from admin_argon.forms import RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth import logout
from accounts.forms import SignUpForm , LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from notification.models import *
from django.contrib.auth.forms import  AuthenticationForm

User = get_user_model()


def notifications(request):
  notifications = AdminNotification.objects.all()
  context = {'notify':notifications}
  return render(request , 'includes/navigation.html' , context)


def register(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
       form.save()
       print("Account created successfully!")
       return redirect('/accounts/login/')
    else:
       print("Registration failed!")
  else:
    form = SignUpForm()

  
  context = { 'form': form }
  return render(request, 'accounts/sign-up.html', context)


class UserLoginView(LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = LoginForm


class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')