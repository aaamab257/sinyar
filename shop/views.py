from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class UserRegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user':serializer.data , 'registered':True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            user_serializer = UserSerializer(user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer({'access': str(refresh.access_token), 'refresh': str(refresh)})
            return Response({'Token':serializer.data , 'user':user_serializer.data})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


class ProductListAPIView(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products':serializer.data})
    

class CategoryListAPIView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    


class SubCategoryProductListAPIView(APIView):
    def post(self, request, format=None):
        subcategory_id = request.data.get('subcategory_id')

        try:
            subcategory = SubCategory.objects.get(pk=subcategory_id)
        except SubCategory.DoesNotExist:
            return Response({'error': 'Subcategory does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubCategorySerializer(subcategory)
        return Response(serializer.data)
    

class FavoriteProductCreateAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        user = request.user
        product_id = request.data.get('product_id')

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        user.favorites.add(product)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)