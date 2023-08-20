from rest_framework import serializers
from accounts.models import User
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "image")


class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = SubCategory
        fields = ("id", "name", "products")


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "image", "subcategories")


class UserSerializer(serializers.ModelSerializer):
    favorites = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "phone", "email", "favorites")


class MarkedCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = IntrestedCategory
        fields = ("id", "user", "category")


class CreateInterestedCategoriesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = IntrestedCategory
        fields = "__all__"

    def create(self, validated_data):
        user = self.context.get("user")
        return IntrestedCategory.objects.create(user=user, **validated_data)
