from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class InstallmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'installment'
    verbose_name = _('Installment')
