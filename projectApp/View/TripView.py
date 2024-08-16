from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from projectApp.Serialzier.DriverSerializer import DriverSerializer
from projectApp.Serialzier.TripSerializer import TripEndSerializer, TripCreateSerializer, TripSerializer, \
    TripHistorySerializer
from projectApp.Serialzier.TruckSerializer import TruckSerializer
from projectApp.models import Trip, Driver, Truck
from decimal import Decimal

class TripListView(APIView):
    def get(self, request, format=None):
        trips = Trip.objects.filter(trip_status=True)

        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # Use TripCreateSerializer for creation
        serializer = TripCreateSerializer(data=request.data)
        if serializer.is_valid():
            trip = serializer.save()
            # Perform any additional logic after saving, if needed
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TripDetailView(APIView):
    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripEndSerializer(trip)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripEndSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        trip = self.get_object(pk)
        serializer = TripEndSerializer(trip, data=request.data, partial=True)
        if serializer.is_valid():
            trip_data = serializer.validated_data
            if 'end_date' in trip_data and 'total_km_driven' in trip_data:
                trip.end_date = trip_data['end_date']
                trip.total_km_driven = trip_data['total_km_driven']
                trip.diesel_consumed = trip_data['diesel_consumed']
                trip.diesel_price = trip_data['diesel_price']
                trip.fare = trip_data['fare']
                trip.other_repair_costs = trip_data['other_repair_costs']
                trip.remarks = trip_data['remarks']
                trip.daily_expenses = trip_data['daily_expenses']
                trip.trip_maintenance_cost = trip_data['trip_maintenance_cost']
                trip.trip_status = False
                trip.driver.on_trip=False
                trip.truck.on_trip=False
                trip.driver.save()
                trip.trip_money_earned = trip.fare * trip.total_km_driven
                trip.truck_avg = trip.total_km_driven / trip.diesel_consumed

                trip.trip_money_spend = ((Decimal(trip.total_km_driven) * Decimal( trip.diesel_price)) + trip.other_repair_costs +
                                         trip.trip_maintenance_cost)+trip.daily_expenses

                #
                trip.total_cash = trip.trip_money_earned - trip.trip_money_spend
                if trip.truck:
                    trip.truck.truck_maintenance_cost+= trip.trip_maintenance_cost
                    trip.truck.total_km_driven += trip.total_km_driven
                    trip.truck.save()

                trip.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        trip = self.get_object(pk)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TripDriver(APIView):
    def get(self, request):
        driver = Driver.objects.all().filter(driver_status=False)
        serializer = DriverSerializer(driver, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class TripTruck(APIView):
    def get(self, request):
        truck = Truck.objects.all().filter(truck_status=False)
        serializer = TruckSerializer(truck, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class TriphistoryListView(APIView):
    def get(self, request, format=None):
        trips = Trip.objects.filter(trip_status=False)

        serializer = TripHistorySerializer(trips, many=True)
        return Response(serializer.data)