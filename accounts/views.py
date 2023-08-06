from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from django.contrib.auth import logout
from django.shortcuts import  redirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class UserRegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'user':serializer.data , 'registered':True}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request, format=None):
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = authenticate(username=phone, password=password)
        if user is not None:
            login(request, user)
            user_serializer = UserSerializer(user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer({'access': str(refresh.access_token), 'refresh': str(refresh)})
            return Response({'Token':serializer.data , 'user':user_serializer.data})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


def user_logout_view(request):
  logout(request)
  return redirect('/admin/login/')

