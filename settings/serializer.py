from rest_framework import serializers
from .models import *

class OnBoardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnBoarding
        fields = ('id', 'title', 'desc')