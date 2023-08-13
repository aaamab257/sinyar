from django.db.models.signals import post_save 
from django.dispatch import receiver
from .models import Request



@receiver(post_save, sender=Request)
def dashboard_update_handler(sender, instance, **kwargs):
    if instance.user.is_staff:
        print(instance.user.id)
        print("Admin update occurred on the dashboard!")