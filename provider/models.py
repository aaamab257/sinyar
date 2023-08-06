from django.db import models
from shop.models import *
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='vendor email address',
        max_length=255,
        unique=True,
    )
    category = models.ForeignKey(Category ,  on_delete=models.CASCADE, related_name='category')
    phone_number = models.CharField(max_length=20 , unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    image = models.ImageField(upload_to='providers/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = _("Provider")
        verbose_name_plural = _("Providers")

    
   
    


class ProviderServices(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Provider ,  on_delete=models.CASCADE, related_name='provider')

    def __str__(self):
        return self.name 