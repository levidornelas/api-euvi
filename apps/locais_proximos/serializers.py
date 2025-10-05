from rest_framework import serializers
from .models import LocaisProximos


class LocaisProximosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocaisProximos
        fields = '__all__'
