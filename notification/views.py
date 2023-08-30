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
from .models import *


# Create your views here.


class GetNotifications(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        notifications = UserMessages.objects.filter(user=user)
        serializer = MessagesSerializer(notifications, many=True)
        public = Notification.objects.all()
        notifiSer = NotificationsSerializer(public, many=True)
        return Response(
            {
                "notifications": {
                    "messages": serializer.data,
                    "public": notifiSer.data,
                }
            }
        )
