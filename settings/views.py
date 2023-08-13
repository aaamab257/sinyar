from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from .serializer import *
from django.utils import translation
# Create your views here.


class OnBoardingListAPIView(APIView):
    def get(self, request, format=None):
        onBoarding = OnBoarding.objects.all()
        serializer = OnBoardingSerializer(onBoarding, many=True)
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            translation.activate(language)
        return Response({'onBoarding': serializer.data})