from rest_framework import serializers
from accounts.models import User
from .models import *


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'category', 'phone_number', 'address')



class ProviderServicesSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ProviderServices
        fields = ('id', 'name', 'provider')