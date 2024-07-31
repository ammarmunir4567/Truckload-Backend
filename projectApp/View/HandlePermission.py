# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from projectApp.Serializer import UserSerializer
from projectApp.models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def update_role(self, request, pk=None):
        user = self.get_object()
        user.role = request.data.get('role')
        user.save()
        return Response({'status': 'role updated'})
