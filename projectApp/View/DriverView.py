from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from django.shortcuts import get_object_or_404
from projectApp.Serialzier.DriverSerializer import DriverSerializer
from projectApp.models import Driver


class DriverListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DriverRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        driver = get_object_or_404(Driver, pk=pk)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    def put(self, request, pk):
        driver = get_object_or_404(Driver, pk=pk)
        serializer = DriverSerializer(driver, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        driver = get_object_or_404(Driver, pk=pk)
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from projectApp.models import Driver
from projectApp.Serialzier.DriverSerializer import DriverSerializer


class ExpiringLicensesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = datetime.now().date()
        three_months_from_now = today + timedelta(days=90)
        drivers = Driver.objects.filter(license_expiry__lte=three_months_from_now)
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)
