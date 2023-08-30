from django.urls import path
from . import views
from dashboard.views import set_language

urlpatterns = [
    # other URLs...
    path(
        "api/categories/", views.CategoryListAPIView.as_view(), name="category-list-api"
    ),
    # GuestCategory
    path(
        "api/guestCategory", views.GuestCategory.as_view(), name="category-list-api"
    ),
    path("api/products/", views.ProductListAPIView.as_view(), name="product-list-api"),
    path(
        "api/subcategories/products/",
        views.SubCategoryProductListAPIView.as_view(),
        name="subcategory-product-list-api",
    ),
    path(
        "api/favorites/",
        views.FavoriteProductCreateAPIView.as_view(),
        name="favorite-product-create-api",
    ),
    # FavoriteRemoveProduct
    path(
        "api/removeFavorites/",
        views.FavoriteRemoveProduct.as_view(),
        name="favorite-product-create-api",
    ),
    path(
        "api/subCategory/",
        views.GetSubCategoryListAPIView.as_view(),
        name="subCategory-list-api",
    ),
    path("set_language/<str:language>", set_language, name="set-language"),
    path(
        "api/markedCategory", views.GetMarkedCategory.as_view(), name="marked_category"
    ),
    # IntrestedCategories
    path(
        "api/makeIntrested",
        views.IntrestedCategories.as_view(),
        name="intrested_category",
    ),
    path(
        "api/makeRequest",
        views.NewRequest.as_view(),
        name="make_request",
    ),

    # GetAllFavoraites

    path(
        "api/getFavoraites",
        views.GetAllFavoraites.as_view(),
        name="getFavo",
    ),

    path(
        "api/getCurrentRequest",
        views.GetCurrentRequests.as_view(),
        name="getCreq",
    ),
    path(
        "api/getPerviousRequest",
        views.GetPerviousRequests.as_view(),
        name="getPreq",
    ),
]
