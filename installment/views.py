from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext
from django.conf import settings
from django.utils import translation

# Create your views here.


class GetPlans(APIView):
    def get(self, request, format=None):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE')
        if language:
            translation.activate(language)
        
        plans = InstallMentsPlans.objects.all()
        serializer = PlansSerializer(plans, many=True)
        return Response({'plans':serializer.data})
    



class MakeInstallment(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request , format=None):
        user = request.user
        serializer = InstallmentsSerializer(context={'user':user } ,data=request.data )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'data':serializer.data , },status=status.HTTP_201_CREATED)
        return Response({'errors':"Errors" , },status=status.HTTP_400_BAD_REQUEST)

        
