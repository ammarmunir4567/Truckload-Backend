
from projectApp.models import Truck
from rest_framework import serializers


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'
