from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Notification(models.Model):
    title = models.CharField(max_length=55, default="")
    message = models.TextField(max_length=255, default="")
    is_opened = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class UserMessages(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name=_('User'))
    title = models.CharField(max_length=55, default="")
    body = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Notification for {self.user.name}"