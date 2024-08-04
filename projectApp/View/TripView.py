from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from projectApp.Serialzier.TripSerializer import TripEndSerializer, TripCreateSerializer
from projectApp.models import Trip


class TripListView(APIView):
    def get(self, request, format=None):
        trips = Trip.objects.all()
        serializer = TripEndSerializer(trips, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TripCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        trip = self.get_object(pk)
        trip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
