# Generated by Django 3.1.1 on 2024-08-15 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_auto_20240814_1911'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='permit',
            unique_together={('region',)},
        ),
    ]
