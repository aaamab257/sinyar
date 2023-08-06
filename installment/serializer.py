from rest_framework import serializers
from .models import *

class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallMentsPlans
        fields = '__all__'


class InstallmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('user')
        return Installment.objects.create(user=user , **validated_data) 