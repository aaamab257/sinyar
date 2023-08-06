from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext
from django.conf import settings
from django.utils import translation
from .serializer import *


class GetAllProviders(APIView):
    def get(self, request, format=None):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response({'providers':serializer.data })
    

class GetServicesOfProvider(APIView):
    def post(self, request , format=None):
        providerId = request.data.get('provider_id')
        services = ProviderServices.objects.filter(provider=providerId)
        serializers = ProviderServicesSerializer(services , many=True)
        return Response({'services':serializers.data })