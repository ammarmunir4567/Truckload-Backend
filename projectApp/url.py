# urls.py
from django.urls import path

from projectApp.View.DriverView import DriverListCreateAPIView, DriverRetrieveUpdateDestroyAPIView
from projectApp.View.TruckView import TruckListCreateAPIView, TruckRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projectApp.View.UserViews import RegisterView, LoginView

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('trucks/', TruckListCreateAPIView.as_view(), name='truck-list-create'),
    path('trucks/<int:pk>/', TruckRetrieveUpdateDestroyAPIView.as_view(), name='truck-detail'),
    path('drivers/', DriverListCreateAPIView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', DriverRetrieveUpdateDestroyAPIView.as_view(), name='driver-detail'),



]
