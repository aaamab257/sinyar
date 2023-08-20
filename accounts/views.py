from requests import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login

from accounts.fcm_services import FCMThread
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
import json

# Create your views here.


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
            send_notification(user.fcm_token , 'Register' , 'Your Account Created Successfully')
            return Response(
                {"user": serializer.data, "registered": True},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    def post(self, request, format=None):
        phone = request.data.get("phone")
        password = request.data.get("password")
        user = authenticate(username=phone, password=password)
        if user is not None:
            login(request, user)
            user_serializer = UserSerializer(user)
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
