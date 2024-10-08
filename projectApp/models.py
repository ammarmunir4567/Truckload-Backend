from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Truck(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
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
    phone_number = models.CharField(max_length=15)
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
    end_date = models.DateField(null=True, blank=True)
    total_km_driven = models.PositiveIntegerField(default=0)
    diesel_consumed=models.PositiveIntegerField(default=0)
    diesel_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    truck_avg=models.FloatField(default=0)
    fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    other_repair_costs = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remarks = models.TextField()

    def calculate_total_cost(self):
        return (self.total_km_driven * self.diesel_price) + self.other_repair_costs

    def calculate_avg(self):
        return(self.total_km_driven/self.diesel_consumed)

    def save(self, *args, **kwargs):
        if self.truck.needs_oil_change():
            raise ValueError("Truck needs an oil change and cannot be assigned to a trip.")
        super().save(*args, **kwargs)
