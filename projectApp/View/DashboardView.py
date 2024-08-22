
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from projectApp.Serialzier.DashboardSerializer import DashboardSerializer
from projectApp.models import Driver, Truck, Trip
from django.db.models import Sum
from django.db.models.functions import Coalesce


class DashboardView(generics.GenericAPIView):
    serializer_class = DashboardSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        drivers_count = Driver.objects.count()
        trucks_count = Truck.objects.count()
        active_trips_count = Trip.objects.filter(trip_status=True).count()
        inactive_drivers_count = Driver.objects.filter(on_trip=False).count()
        inactive_trucks_count = Truck.objects.filter(on_trip=False).count()
        netProfit = Trip.objects.aggregate(total_cash_sum=Coalesce(Sum('total_cash'), 0))['total_cash_sum']

        data = {
            'drivers': drivers_count,
            'trucks': trucks_count,
            'activeTrips': active_trips_count,
            'inactiveDrivers': inactive_drivers_count,
            'inactiveTrucks': inactive_trucks_count,
            'netProfit': netProfit,
        }

        return Response(data)
