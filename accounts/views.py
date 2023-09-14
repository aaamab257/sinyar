from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.fcm_services import FCMThread
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from rest_framework import generics, status, views, permissions
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from .utils import Util
from drf_yasg.utils import swagger_auto_schema
import jwt
from drf_yasg import openapi
from django.http import HttpResponsePermanentRedirect
import os
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth import get_user_model


User = get_user_model()



# Create your views here.

class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


def send_notification(user_fcm_device, title, bodyContent):
    header = {
        "Authorization": "key=AAAAp8z7mtY:APA91bHfVBSuElVJ8pg_qvpDjt8xjMTqUJ1LPira1OblHh5CL0PqSvocEELfc341GurquPoE5zvcRjhJOTIODv9qGzgZnar2Gd3cR102R8AnkndYMKhiYlDIvBncx_rAnsd7omld3URs",
        "Content-Type": "application/json",
    }

    body = {
        "to": user_fcm_device,
        "notification": {"body": bodyContent, "title": title},
    }

    response = requests.post(
        "https://fcm.googleapis.com/fcm/send",
        headers=header,
        json=body,
    )
    if response.status_code == 200:
        data = response.json()


class UserRegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            serializerToken = TokenSerializer(
                {"access": str(refresh.access_token), "refresh": str(refresh)}
            )
            send_notification(user.fcm_token , 'Register' , 'Your Account Created Successfully')
            return Response(
                {"user": serializer.data, 'token':serializerToken.data,  "registered": True},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request, format=None):
        phone = request.data.get("phone")
        password = request.data.get("password")
        fcm = request.data.get("fcm_token")
        user = authenticate(username=phone, password=password)
        if user is not None:
            login(request, user)
            user_serializer = UserSerializer(user)
            user.fcm_token = fcm
            user.save()
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(
                {"access": str(refresh.access_token), "refresh": str(refresh)}
            )
            send_notification(
                user_fcm_device=user.fcm_token,
                bodyContent=f"Welcome back {user.name}",
                title="Login",
            )
            # send_push_notification()
            return Response(
                {
                    "Token": serializer.data,
                    "user": user_serializer.data,
                    "user_id": user.pk,
                }
            )
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )

class ChangePassword(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        old_pass = request.data.get('old_password')
        new_pass = request.data.get('new_password')
        user = request.user
        if not user.check_password(old_pass):
            return Response({'status': status.HTTP_404_NOT_FOUND,'user' :"Old password is Invalid" }, status=status.HTTP_404_NOT_FOUND)
        if user is None:
            return Response({'status': status.HTTP_404_NOT_FOUND,'user' :"User Not Found" }, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = UserSerializer(user)
            user.set_password(new_pass)
            user.save()
            return Response({'status': status.HTTP_200_OK,'user' :serializer.data})





def user_logout_view(request):
    logout(request)
    return redirect("/admin/login/")


def send_push_notification():
    # Define the FCM API endpoint URL
    api_url = "https://fcm.googleapis.com/fcm/send"

    # Define the server key obtained from the Firebase console
    server_key = "AAAAp8z7mtY:APA91bHfVBSuElVJ8pg_qvpDjt8xjMTqUJ1LPira1OblHh5CL0PqSvocEELfc341GurquPoE5zvcRjhJOTIODv9qGzgZnar2Gd3cR102R8AnkndYMKhiYlDIvBncx_rAnsd7omld3URs"

    # Define the notification payload
    payload = {
        "to": "/topics/all",
        "notification": {"body": "Hello World There a new update", "title": "Updates"},
    }

    # Define the headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"key={server_key}",
    }

    # Make the API request
    response = requests.post(api_url, json=payload, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        print("Push notification sent successfully.")
    else:
        print("Failed to send push notification.")





def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            phone = form.cleaned_data.get("phone")
            password = form.cleaned_data.get("password")
            user = authenticate(username=phone, password=password)
            if user is not None:
                login(request, user)
                return redirect("/login")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


class GetUserInfo(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user= request.user
        if user is None:
            return Response({'status': status.HTTP_404_NOT_FOUND, 'user' :"User Not Found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = UserSerializer(user)
            return Response({'status': status.HTTP_200_OK,'user' :serializer.data}, status=status.HTTP_200_OK)
        

class EditProfile(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self , request , format=None):
        name = request.data.get('name')
        email = request.data.get('email')
        user = request .user 
        if user is None: 
            return Response({'user':'Not Found' , 'status':status.HTTP_404_NOT_FOUND})
        else:
            user.name = name 
            user.email= email 
            user.save()
            serializer = UserSerializer(user)
            return Response({'user':serializer.data , 'status':status.HTTP_200_OK})