from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from projectApp.Serialzier.TruckSerializer import TruckSerializer, TruckPermitSerializer


class TruckListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trucks = Truck.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            truck = serializer.save()
            return Response(TruckSerializer(truck).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from projectApp.models import Truck

class TruckRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        truck = get_object_or_404(Truck, pk=pk)
        serializer = TruckSerializer(truck)
        return Response(serializer.data)

    def put(self, request, pk):
        truck = get_object_or_404(Truck, pk=pk)
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            truck = serializer.save()
            return Response(TruckSerializer(truck).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        truck = get_object_or_404(Truck, pk=pk)
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from datetime import timedelta, date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ExpiringPermitsView(APIView):
    def get(self, request):
        three_months_from_now = date.today() + timedelta(days=90)
        trucks = Truck.objects.filter(
            permits__expiry_date__lte=three_months_from_now
        ).distinct()
        serializer = TruckPermitSerializer(trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
