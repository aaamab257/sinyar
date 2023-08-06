from django.urls import include, path
from .views import *



urlpatterns = [
    path('getProviders', GetAllProviders.as_view() , name='getProviders'),
    path('getProviderServices', GetServicesOfProvider.as_view() , name='getProviderServices'),

    # GetServicesOfProvider
    
]