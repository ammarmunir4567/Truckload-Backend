# urls.py
from django.urls import path

from .DriverView import DriverListCreateAPIView, DriverRetrieveUpdateDestroyAPIView
from .TruckView import TruckListCreateAPIView, TruckRetrieveUpdateDestroyAPIView
from .views import SignUpView, LoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view()),
    path('trucks/', TruckListCreateAPIView.as_view(), name='truck-list-create'),
    path('trucks/<int:pk>/', TruckRetrieveUpdateDestroyAPIView.as_view(), name='truck-detail'),
    path('drivers/', DriverListCreateAPIView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', DriverRetrieveUpdateDestroyAPIView.as_view(), name='driver-detail'),

]
