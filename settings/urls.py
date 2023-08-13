from django.contrib import admin
from django.urls import include, path
from .views import * 

urlpatterns = [
    path('onBoarding' , OnBoardingListAPIView.as_view() , name='images' ),
    path('offers' , OffersListAPIView.as_view() , name='offers' ),
]
