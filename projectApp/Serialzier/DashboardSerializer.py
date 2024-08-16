from rest_framework import serializers


class DashboardSerializer(serializers.Serializer):
    drivers = serializers.IntegerField()
    trucks = serializers.IntegerField()
    activeTrips = serializers.IntegerField()
    inactiveDrivers = serializers.IntegerField()
    inactiveTrucks = serializers.IntegerField()
    netProfit = serializers.DecimalField(max_digits=10, decimal_places=2)
