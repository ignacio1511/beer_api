from rest_framework import serializers
from .models import Dispenser

class DispenserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispenser
        fields = '__all__'
