from django.db import models
from accounts.models import User
# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_opened = models.BooleanField(default=False)

    def __str__(self):
        return self.message