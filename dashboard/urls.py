from django.urls import path
from admin_black.views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="home"),
    path("set_language/<str:language>", views.set_language, name="set-language"),
    path("accounts/auth-signup/", auth_signup, name="auth_signup"),
    path("accounts/auth-signin/", AuthSignin.as_view(), name="auth_signin"),
    path(
        "accounts/forgot-password/",
        UserPasswordResetView.as_view(),
        name="forgot_password",
    ),
    path('rtl/', rtl, name='rtl'),
    path(
        "accounts/password-reset-confirm/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/password-change/",
        UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password-change-done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "accounts/password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(
        "accounts/password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path("accounts/logout/", user_logout_view, name="logout"),
]
