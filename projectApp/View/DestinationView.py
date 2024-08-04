from rest_framework import generics

from projectApp.Serialzier.DestinationSerialzier import DestinationSerializer
from projectApp.models import Destination


class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
