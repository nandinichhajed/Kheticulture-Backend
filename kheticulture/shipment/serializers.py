from store.models import Product
from django.db.models import fields
from .models import Shipment, Shippment_Tracking
from rest_framework import serializers
from django.conf import settings

class ShipmentSerializer(serializers.ModelSerializer):
    order = serializers.IntegerField
    shipment_status = serializers.CharField(max_length = 20)
    shipment_date = serializers.DateTimeField()

    class Meta:
        model = Shipment
        fields = (
            'order',
            'shipment_status',
            'shipment_date'
        )

    def update(self, instance, validated_data):
            instance.shipment_status = validated_data.get('shipment_status')
            instance.save()
            return instance
