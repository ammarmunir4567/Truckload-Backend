# urls.py
from django.urls import path

from projectApp.View.DriverView import DriverListCreateAPIView, DriverRetrieveUpdateDestroyAPIView
from projectApp.View.TruckView import TruckListCreateAPIView, TruckRetrieveUpdateDestroyAPIView
from projectApp.View.UserViews import SignUpView, LoginView, ChangePasswordView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view()),
    path('trucks/', TruckListCreateAPIView.as_view(), name='truck-list-create'),
    path('trucks/<int:pk>/', TruckRetrieveUpdateDestroyAPIView.as_view(), name='truck-detail'),
    path('drivers/', DriverListCreateAPIView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', DriverRetrieveUpdateDestroyAPIView.as_view(), name='driver-detail'),
    path('change_password/', ChangePasswordView.as_view()),


]
