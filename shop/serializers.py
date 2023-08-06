from rest_framework import serializers
from accounts.models import User
from .models import *




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image')



class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'products')




class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategories')


class UserSerializer(serializers.ModelSerializer):
    favorites = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'favorites')