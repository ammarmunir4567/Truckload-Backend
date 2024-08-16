# urls.py
from django.urls import path


from projectApp.View.DashboardView import DashboardView
from projectApp.View.DestinationView import DestinationListCreateView, DestinationRetrieveUpdateDestroyView
from projectApp.View.DriverView import DriverListCreateAPIView, DriverRetrieveUpdateDestroyAPIView, \
    ExpiringLicensesAPIView
from projectApp.View.TripView import TripDetailView, TripListView, TripTruck, TripDriver, TriphistoryListView
from projectApp.View.TruckView import TruckListCreateAPIView, TruckRetrieveUpdateDestroyAPIView, ExpiringPermitsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projectApp.View.UserViews import RegisterView, LoginView, ChangePasswordView, LogoutView, UserListView, \
    UserDetailView, UpdateUserView


urlpatterns = [


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/update/', UpdateUserView.as_view(), name='update_user'),

    path('trucks/', TruckListCreateAPIView.as_view(), name='truck-list-create'),
    path('trucks/<int:pk>/', TruckRetrieveUpdateDestroyAPIView.as_view(), name='truck-detail'),
    path('trucks/expiring-permits/', ExpiringPermitsView.as_view(), name='expiring-permits'),

    path('drivers/', DriverListCreateAPIView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', DriverRetrieveUpdateDestroyAPIView.as_view(), name='driver-detail'),
    path('drivers/expiring-licenses/', ExpiringLicensesAPIView.as_view(), name='expiring-licenses'),


    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('destinations/', DestinationListCreateView.as_view(), name='destination-list-create'),
    path('destinations/<int:pk>/', DestinationRetrieveUpdateDestroyView.as_view()),

    path('trips/', TripListView.as_view(), name='trip-list'),
    path('trips/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    path('tripsHistory', TriphistoryListView.as_view(), name='trip-detail'),

    path('TripTruck/', TripTruck.as_view()),
    path('TripDriver/', TripDriver.as_view()),



]
