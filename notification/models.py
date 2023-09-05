from datetime import timezone
from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Notification(models.Model):
    title = models.CharField(max_length=55, default="")
    message = models.TextField(max_length=255, default="")
    is_opened = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True )
    

    # , default='2023-08-27T11:56:26.123140Z'
    def __str__(self):
        return self.title


class UserMessages(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name=_('User'))
    title = models.CharField(max_length=55, default="")
    body = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f"Notification for {self.user.name}"
    

class AdminNotification(models.Model):
    title = models.CharField(max_length=55, default="")
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


    def __str__(self):
        return f"Notification Title :{self.title}"