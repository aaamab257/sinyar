from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import *
import requests


User = get_user_model()

@receiver(post_save, sender=Notification)
def create_notification(sender, instance, created, **kwargs):
    if instance.title:
        if instance.title:
            header = {
                "Authorization": "key=AAAAp8z7mtY:APA91bHfVBSuElVJ8pg_qvpDjt8xjMTqUJ1LPira1OblHh5CL0PqSvocEELfc341GurquPoE5zvcRjhJOTIODv9qGzgZnar2Gd3cR102R8AnkndYMKhiYlDIvBncx_rAnsd7omld3URs",
                "Content-Type": "application/json",
            }
            body = {
                "notification": {
                    "title": instance.title,
                    "body": instance.message,
                },
                "data": {
                    "title": instance.title,
                    "body": instance.message,
                },
                "to": "/topics/all",  # Send to a topic named "all" to target all devices
            }
            response = requests.post(
                "https://fcm.googleapis.com/fcm/send",
                headers=header,
                json=body,
            )
            if response.status_code == 200:
                data = response.json()
                print(f"{data}")


@receiver(post_save, sender=User)
def send_notification(sender, instance, created, **kwargs):
    if created:
        title = "Users Registrations"
        message = f"New user registered: {instance.email}"
        notification = AdminNotification.objects.create(message=message )
        notification.save()