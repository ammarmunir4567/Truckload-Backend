from rest_framework import serializers
from projectApp.models import Truck, Permit


class PermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permit
        fields = ['region', 'expiry_date']


class TruckSerializer(serializers.ModelSerializer):
    permits = PermitSerializer(many=True)

    class Meta:
        model = Truck
        fields = '__all__'

    def create(self, validated_data):
        permits_data = validated_data.pop('permits', [])
        truck = Truck.objects.create(**validated_data)
        for permit_data in permits_data:
            permit, created = Permit.objects.get_or_create(**permit_data)
            truck.permits.add(permit)
        return truck

    def update(self, instance, validated_data):
        permits_data = validated_data.pop('permits', [])
        # Update instance attributes
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        # Update permits
        instance.permits.clear()
        for permit_data in permits_data:
            permit, created = Permit.objects.get_or_create(**permit_data)
            instance.permits.add(permit)
        return instance


class TruckPermitSerializer(serializers.ModelSerializer):
    permits = PermitSerializer(many=True)

    class Meta:
        model = Truck
        fields = ['make', 'model', 'license_plate', 'permits']





class TruckOilChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['id', 'make', 'model', 'year', 'license_plate', 'total_km_driven', 'last_oil_change_km']


