# urls.py
from django.urls import path


from projectApp.View.DashboardView import DashboardView
from projectApp.View.DriverView import DriverListCreateAPIView, DriverRetrieveUpdateDestroyAPIView
from projectApp.View.TruckView import TruckListCreateAPIView, TruckRetrieveUpdateDestroyAPIView
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
    path('drivers/', DriverListCreateAPIView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', DriverRetrieveUpdateDestroyAPIView.as_view(), name='driver-detail'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]
