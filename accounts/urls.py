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
    
    path("getUserInfo", views.GetUserInfo.as_view(), name="user_info"),
    path('changePassword' , views.ChangePassword.as_view() , name='changePass'),
    path('editProfile' , views.EditProfile.as_view() , name= 'edit_profile'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
