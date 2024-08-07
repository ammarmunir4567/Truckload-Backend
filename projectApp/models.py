from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='viewer')


class Truck(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField(null=True, blank=True)
    token_price = models.IntegerField(null=True, blank=True)
    region_permit = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    on_trip = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[
        ('Active', 'Active'),
        ('In Maintenance', 'In Maintenance'),
        ('Out of Service', 'Out of Service')
    ])
    last_oil_change_km = models.PositiveIntegerField(default=0)
    total_km_driven = models.PositiveIntegerField(default=0)

    def needs_oil_change(self):
        return self.total_km_driven - self.last_oil_change_km >= 300


class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=30, unique=True)
    license_expiry = models.DateField()
    phone_number = models.CharField(max_length=15)
    CNIC = models.CharField(max_length=100)
    on_trip = models.BooleanField(default=False)
    address = models.TextField()
    hire_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('Active', 'Active'),
        ('On Leave', 'On Leave')
    ])


class Destination(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()


class Trip(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_km_driven = models.PositiveIntegerField(default=0)
    diesel_consumed = models.PositiveIntegerField(default=0)
    diesel_price = models.DecimalField(max_digits=10, decimal_places=2)
    truck_avg = models.FloatField(default=0)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    other_repair_costs = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remarks = models.TextField()
    trip_status = models.BooleanField(default=False)
    trip_money_spend=models.IntegerField(default=0)
    trip_money_earned = models.IntegerField(default=0)
    total_cash=models.IntegerField(default=0)




