from rest_framework import serializers
from accounts.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
      model = User
      fields=['email', 'name', 'password', 'password2' , 'date_of_birth' , 'phone' ,'is_admin']
      extra_kwargs={
        'password':{'write_only':True}
      }

  # Validating Password and Confirm Password while Registration
    def validate(self, attrs):
      password = attrs.get('password')
      password2 = attrs.get('password2')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      return attrs

    def create(self, validate_data):
      return User.objects.create_user(**validate_data)

class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


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


# class UserSerializer(serializers.ModelSerializer):
#     favorites = ProductSerializer(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'favorites')