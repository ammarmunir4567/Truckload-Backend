# UserViews.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from projectApp.Serializer import TruckSerializer
from projectApp.models import Truck


class TruckListCreateAPIView(APIView):
    def get(self, request):
        trucks = Truck.objects.all()
        serializer = TruckSerializer(trucks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TruckRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        truck = get_object_or_404(Truck, pk=pk)
        serializer = TruckSerializer(truck)
        return Response(serializer.data)

    def put(self, request, pk):
        truck = get_object_or_404(Truck, pk=pk)
        serializer = TruckSerializer(truck, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        truck = get_object_or_404(Truck, pk=pk)
        truck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
