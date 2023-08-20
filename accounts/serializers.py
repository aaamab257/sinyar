from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



class UserSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
      model = User
      fields=['email', 'name', 'password', 'password2' , 'date_of_birth' ,'fcm_token', 'phone' ,'is_admin' , 'is_user' ,'is_vendor']
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