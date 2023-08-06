from django.urls import path
from .views import *


urlpatterns = [
    path("getPlans", GetPlans.as_view(), name="plansList"),
    path("addInstallments", MakeInstallment.as_view(), name="installments"),
]
