# Generated by Django 3.1.1 on 2024-08-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0009_trip_daily_expenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='truck_maintenance_cost',
            field=models.IntegerField(default=0),
        ),
    ]
