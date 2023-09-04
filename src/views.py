from django.shortcuts import render, redirect
from admin_argon.forms import RegistrationForm, LoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.contrib.auth import logout
from accounts.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()


@login_required
def index(request):
  return render(request, 'pages/dashboard.html')


def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
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