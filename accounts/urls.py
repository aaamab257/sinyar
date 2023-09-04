from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    # other URLs...
    path("register", views.UserRegisterAPIView.as_view(), name="user-register-api"),
    path("login", views.UserLoginAPIView.as_view(), name="user-login-api"),
    
    
    path("login/", views.login_view, name="login"),
    path("register/", views.register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
