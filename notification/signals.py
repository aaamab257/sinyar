from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Notification

@receiver(post_save, sender=User)
def create_notification(sender, instance, created, **kwargs):
    if created:
        # Check if the user is an admin
        if instance.is_staff:
            message = f"New request received from user {instance.username}"
            notification = Notification(user=instance, message=message)
            notification.save()