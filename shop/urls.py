from django.urls import path
from . import views

urlpatterns = [
    # other URLs...
    path('api/register', views.UserRegisterAPIView.as_view(), name='user-register-api'),
    path('api/login', views.UserLoginAPIView.as_view(), name='user-login-api'),
    path('api/categories/', views.CategoryListAPIView.as_view(), name='category-list-api'),
    path('api/products/', views.ProductListAPIView.as_view(), name='product-list-api'),
    path('api/subcategories/products/', views.SubCategoryProductListAPIView.as_view(), name='subcategory-product-list-api'),
    path('api/favorites/', views.FavoriteProductCreateAPIView.as_view(), name='favorite-product-create-api'),
]