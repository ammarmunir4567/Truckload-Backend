# serializers.py
from rest_framework import serializers
from .models import Driver, Trip
from .models import Truck
from django.contrib.auth import get_user_model  # Import the custom user model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'],
                                        password=validated_data['password'],
                                        first_name=validated_data.get('first_name', ''),
                                        last_name=validated_data.get('last_name', ''))
        return user


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    avg = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = [
            'id', 'truck', 'driver', 'destination', 'start_date', 'end_date',
            'total_km_driven', 'diesel_consumed', 'diesel_price', 'truck_avg',
            'fare', 'other_repair_costs', 'remarks', 'total_cost', 'avg'
        ]

    def get_total_cost(self, obj):
        return obj.calculate_total_cost()

    def get_avg(self, obj):
        return obj.calculate_avg()
