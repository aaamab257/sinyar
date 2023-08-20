from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Request
import requests
from django.contrib.admin.models import LogEntry


@receiver(pre_save, sender=Request)
def dashboard_update_handler(sender, instance, **kwargs):
    print(instance.status)
    if instance.user.is_staff:
        header = {
            "Authorization": "key=AAAAp8z7mtY:APA91bHfVBSuElVJ8pg_qvpDjt8xjMTqUJ1LPira1OblHh5CL0PqSvocEELfc341GurquPoE5zvcRjhJOTIODv9qGzgZnar2Gd3cR102R8AnkndYMKhiYlDIvBncx_rAnsd7omld3URs",
            "Content-Type": "application/json",
        }

        if instance.status == "a":
            body = {
                "to": instance.user.fcm_token,
                "notification": {
                    "body": "Your request accepted",
                    "title": "Installment request",
                },
            }
        else:
            body = {
                "to": instance.user.fcm_token,
                "notification": {
                    "body": "Your request Refused",
                    "title": "Installment request",
                },
            }

        response = requests.post(
            "https://fcm.googleapis.com/fcm/send",
            headers=header,
            json=body,
        )
        if response.status_code == 200:
            data = response.json()
