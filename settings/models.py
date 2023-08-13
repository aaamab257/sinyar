from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class OnBoarding(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    image = models.ImageField(upload_to='onBoarding/')

    class Meta:
        verbose_name_plural = _("OnBoarding")
        verbose_name = _("OnBoarding")

    def __str__(self):
        return self.title
    


class OffersSlider(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='offersSliders/')
    class Meta:
        verbose_name_plural = _("OffersSlider")
        verbose_name = _("OffersSlider")

    def __str__(self):
        return self.title

