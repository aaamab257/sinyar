"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from dashboard.views import set_language
from .views import *
from django.contrib.auth import views as auth_views

from django.contrib.auth import get_user_model
User = get_user_model()



admin.site.site_header = "Sinyar Admin"
admin.site.index_title = "Welcome to Sinyar Dashboard"
admin.site.site_title = "Sinyar"


urlpatterns = i18n_patterns(
    # path('', include('dashboard.urls')),
    path("admin/", admin.site.urls),
    # path("dashboard/", include('admin_black.urls')),
    path("auth/" , include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('installment/', include('installment.urls')),
    path('provider/', include('provider.urls')),
    path('settings/', include('settings.urls')),
    path('notifications/', include('notification.urls')),
    path("set_language/<str:language>", set_language, name="set-language"),
    # path("", include("accounts.urls")), # Auth routes - login / register
    # path("", include("home.urls")), 
    # path('', index , name='index'),
    path('', include("admin_argon.urls")), 
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/logout/',user_logout_view, name='logout'),
    path('register/', register, name='register'),
    path('accounts/password-change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),       

    prefix_default_language=False
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


