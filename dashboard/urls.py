from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("set_language/<str:language>", views.set_language, name="set-language"),
]