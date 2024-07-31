from projectApp.models import Trip
from rest_framework import serializers


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
