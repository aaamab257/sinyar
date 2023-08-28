from django.urls import path
from .views import *


urlpatterns = [
    path("getNotifications", GetNotifications.as_view(), name="notifications_list"),
    
]
