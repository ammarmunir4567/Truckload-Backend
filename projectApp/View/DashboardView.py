from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):

        data = {
            'drivers': 10,
            'trucks': 5,
            'activeTrips': 3,
            'netProfit': 5000.00,
            'inactiveDrivers': 2,
            'inactiveTrucks': 1,
            'cities': ['New York', 'Los Angeles', 'Chicago'],
        }
        return Response(data)
