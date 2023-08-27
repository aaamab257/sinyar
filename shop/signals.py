from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Request
import requests
from django.contrib.admin.models import LogEntry
from notification.models import *


@receiver(pre_save, sender=Request)
def dashboard_update_handler(sender, instance, **kwargs):
    print(instance.status)
    title = ""
    bodyM = ""
    if instance.status:
        header = {
            "Authorization": "key=AAAAp8z7mtY:APA91bHfVBSuElVJ8pg_qvpDjt8xjMTqUJ1LPira1OblHh5CL0PqSvocEELfc341GurquPoE5zvcRjhJOTIODv9qGzgZnar2Gd3cR102R8AnkndYMKhiYlDIvBncx_rAnsd7omld3URs",
            "Content-Type": "application/json",
        }

        if instance.status == "a":
            title = "Your request Accepted"
            bodyM = "Installment request"
            body = {
                "to": instance.user.fcm_token,
                "notification": {
                    "body": bodyM,
                    "title": title,
                },
            }
        elif instance.status == "p":
            title = "Your request Pending"
            bodyM = "Installment request"
            body = {
                "to": instance.user.fcm_token,
                "notification": {
                    "body": bodyM,
                    "title": title,
                },
            }

        else:
            title = "Your request Refused"
            bodyM = "Installment request"
            body = {
                "to": instance.user.fcm_token,
                "notification": {
                    "body": bodyM,
                    "title": title,
                },
            }

        response = requests.post(
            "https://fcm.googleapis.com/fcm/send",
            headers=header,
            json=body,
        )
        if response.status_code == 200:
            message = UserMessages.objects.create(
                user=instance.user, title=title, body=bodyM
            )
            message.save()
            data = response.json()
