from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import requests
from .models import *


@receiver(post_save, sender=OffersSlider)
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
                    "body": "New offer added",
                },
                "data": {"title": instance.title, "body": instance.title, "action": "home"},
                "to": "/topics/all",
            }
            response = requests.post(
                "https://fcm.googleapis.com/fcm/send",
                headers=header,
                json=body,
            )
            if response.status_code == 200:
                data = response.json()
                print(f"{data}")
