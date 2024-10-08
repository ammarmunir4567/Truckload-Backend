# Generated by Django 3.1.1 on 2024-07-21 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('license_number', models.CharField(max_length=30, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('hire_date', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('On Leave', 'On Leave')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('license_plate', models.CharField(max_length=20, unique=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In Maintenance', 'In Maintenance'), ('Out of Service', 'Out of Service')], max_length=20)),
            ],
        ),
    ]
