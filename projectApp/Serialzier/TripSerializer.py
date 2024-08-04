from rest_framework import serializers
from projectApp.models import Trip


class TripCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['truck', 'driver', 'destination', 'start_date']


class TripSerializer(serializers.ModelSerializer):
    truck_license_plate = serializers.SerializerMethodField()
    driver_full_name = serializers.SerializerMethodField()
    destination_name = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = ['id', 'truck_license_plate', 'driver_full_name', 'destination_name', 'start_date']

    def get_truck_license_plate(self, obj):
        return obj.truck.license_plate if obj.truck else None

    def get_driver_full_name(self, obj):
        if obj.driver:
            return f"{obj.driver.first_name} {obj.driver.last_name}"
        return None

    def get_destination_name(self, obj):
        return obj.destination.name if obj.destination else None


class TripEndSerializer(serializers.ModelSerializer):
    truck_license_plate = serializers.SerializerMethodField()
    driver_full_name = serializers.SerializerMethodField()
    destination_name = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = ['id', 'truck_license_plate', 'driver_full_name', 'destination_name', 'start_date', 'end_date',
                  'total_km_driven', 'diesel_consumed', 'diesel_price', 'fare', 'other_repair_costs'
            , 'remarks']

    def get_truck_license_plate(self, obj):
        return obj.truck.license_plate if obj.truck else None

    def get_driver_full_name(self, obj):
        if obj.driver:
            return f"{obj.driver.first_name} {obj.driver.last_name}"
        return None

    def get_destination_name(self, obj):
        return obj.destination.name if obj.destination else None
