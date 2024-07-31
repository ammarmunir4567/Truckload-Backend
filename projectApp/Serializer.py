# serializers.py
from rest_framework import serializers
from .models import Driver, Trip, CustomUser
from .models import Truck
from django.contrib.auth import get_user_model  # Import the custom user model
#
# User = get_user_model()
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'first_name', 'last_name', 'password']
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(email=validated_data['email'],
#                                         password=validated_data['password'],
#                                         first_name=validated_data.get('first_name', ''),
#                                         last_name=validated_data.get('last_name', ''))
#         return user
#

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#

# serializers.py
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']


# serializers.py
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])


# myapp/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("User is deactivated.")
            else:
                raise serializers.ValidationError("Unable to login with provided credentials.")
        else:
            raise serializers.ValidationError("Must provide username and password.")
        return data

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField()
    avg = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = [
            'id', 'truck', 'driver', 'destination', 'start_date', 'end_date',
            'total_km_driven', 'diesel_consumed', 'diesel_price', 'truck_avg',
            'fare', 'other_repair_costs', 'remarks', 'total_cost', 'avg'
        ]

    def get_total_cost(self, obj):
        return obj.calculate_total_cost()

    def get_avg(self, obj):
        return obj.calculate_avg()
