from store.models import Product
from django.db.models import fields
from .models import Shipment, Shippment_Tracking
from orders.models import Order
from rest_framework import serializers
from django.conf import settings

class ShipmentSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(),
                                                  many=False) 
    shipment_status = serializers.CharField(max_length=150)
    delivery_status = serializers.CharField(max_length=150)
    description = serializers.CharField()

    class Meta:
        model = Shipment
        fields = (
            'order',
            'shipment_status',
            'delivery_status',
            'description'
        )
    
    def create(self, validated_data):
        return Shipment.objects.create(**validated_data)

class ShipmentStatusSerializer(serializers.ModelSerializer):
    shipment_status = serializers.CharField(max_length = 20)

    class Meta:
        model = Shipment
        fields = (
            'order',
            'shipment_status'
        )

    def update(self, instance, validated_data):
            instance.shipment_status = validated_data.get('shipment_status')
            instance.save()
            return instance
