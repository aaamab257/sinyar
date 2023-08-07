from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from dateutil.relativedelta import relativedelta
from django.utils.timezone import now
from accounts.models import User
from datetime import date, timedelta
from django.utils.translation import gettext_lazy as _
# Create your models here.



class InstallMentsPlans(models.Model):
    num_installments = models.PositiveIntegerField(default=1 ,validators=[MinValueValidator(3), MaxValueValidator(100)] , verbose_name='Months' )
    interest = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)] , default=10)

    class Meta:
        ordering = ['num_installments']


    def __str__(self):
        return f'Installment #{self.num_installments} with intrest #{self.interest}'
    
    class Meta:
        verbose_name = _('InstallMentsPlans')
        verbose_name_plural = _('InstallMentsPlans')


class Installment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name=_('User') , default="" )
    amount = models.DecimalField(max_digits=10, decimal_places=2,)
    due_date = models.DateTimeField(auto_now_add=True, null=True )
    is_paid = models.BooleanField(default=False)
    plan = models.ForeignKey(InstallMentsPlans , on_delete=models.CASCADE , verbose_name="Plan" )
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_approved = models.BooleanField()
    duration = models.IntegerField(null=True)

    def __str__(self):
        return f'Installment #{self.pk} for order #{self.user}'
    
    @property
    def months(self):
        if self.start_date and self.end_date:
            delta = relativedelta(self.end_date, self.start_date)
            return delta.years * 12 + delta.months
        return None

    @property
    def is_approved(self):
        return self.start_date is not None and self.end_date is not None
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Only calculate due date for new installments
            today = date.today()
            months = self.duration
            self.due_date = today + timedelta(days=months * 30)  # Assuming 30 days per month

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Installment')
        verbose_name_plural = _('Installment')
   

    

