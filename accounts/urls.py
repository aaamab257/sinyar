from django.urls import path
from . import views


urlpatterns = [
    # other URLs...
    path('register', views.UserRegisterAPIView.as_view(), name='user-register-api'),
    path('login', views.UserLoginAPIView.as_view(), name='user-login-api'),
    path('logout', views.user_logout_view, name='logout'),
]