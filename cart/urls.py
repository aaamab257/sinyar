from django.urls import path
from .views import *

urlpatterns = [
    # other URLs...
    path('api/add/', AddToCartAPIView.as_view(), name='add-to-cart-api'),
    path('api/remove/', RemoveFromCartAPIView.as_view(), name='remove-from-cart-api'),
]