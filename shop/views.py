from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext
from django.conf import settings
from django.utils import translation


class ProductListAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        message = gettext("Hello, World!")
        language = request.META.get("HTTP_ACCEPT_LANGUAGE")
        if language:
            translation.activate(language)
        return Response({"products": serializer.data, "msg": message})


class CategoryListAPIView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        language = request.META.get("HTTP_ACCEPT_LANGUAGE")
        if language:
            translation.activate(language)
        return Response({"categories": serializer.data})


class GetSubCategoryListAPIView(APIView):
    def post(self, request, format=None):
        category_id = request.data.get("category_id")
        sub_categories = SubCategory.objects.filter(parent=category_id)
        serializer = SubCategorySerializer(sub_categories, many=True)
        language = request.META.get("HTTP_ACCEPT_LANGUAGE")
        if language:
            translation.activate(language)
        return Response({"subCategories": serializer.data})


class SubCategoryProductListAPIView(APIView):
    def post(self, request, format=None):
        subcategory_id = request.data.get("subcategory_id")

        try:
            subcategory = SubCategory.objects.get(pk=subcategory_id)
        except SubCategory.DoesNotExist:
            return Response(
                {"error": "Subcategory does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = SubCategorySerializer(subcategory)
        language = request.META.get("HTTP_ACCEPT_LANGUAGE")
        if language:
            translation.activate(language)
        return Response({"products": serializer.data})


class FavoriteProductCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        product_id = request.data.get("product_id")

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product does not exist."}, status=status.HTTP_404_NOT_FOUND
            )

        user.favorites.add(product)
        user_serializer = UserSerializer(user)
        language = request.META.get("HTTP_ACCEPT_LANGUAGE")
        if language:
            translation.activate(language)
        return Response(user_serializer.data)


class GetMarkedCategory(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        marked_category = IntrestedCategory.objects.filter(user=user)
        serializer = MarkedCategorySerializer(marked_category, many=True)
        return Response({"intrested": serializer.data})


class IntrestedCategories(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        user = request.user
        serializer = CreateInterestedCategoriesSerializer(
            context = {"user": user}, data=request.data
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "intrested": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "errors": "Errors",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
