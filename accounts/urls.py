from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views


urlpatterns = [
    # other URLs...
    path("register", views.UserRegisterAPIView.as_view(), name="user-register-api"),
    path("login", views.UserLoginAPIView.as_view(), name="user-login-api"),
    path("logout", views.user_logout_view, name="logout"),
    path(r'password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
