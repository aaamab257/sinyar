from rest_framework import serializers
from .models import *


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields= '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    # public = NotificationsSerializer(many=True)

    class Meta:
        model = UserMessages
        fields= ('user','title','body','created_at' )