from django.conf import settings
from . import models
from .models import Order
from .models import OrderItem
from account.serializers import CustomerSerializer
from rest_framework import serializers
from orders.validators import (
    UniqueUpdateValidator,
    UniqueUpdateDBValidator,
    UniqueUpdateStatusValidator
)
from tractor.serializers import TractorSerializer

class OrderDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'order', 
            'quantity',
            'price',
        )
        validators = [
            UniqueUpdateValidator()
        ]


class OrderDetailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'order', 
            'quantity',
            'price',
        )
    validators = [
        UniqueUpdateStatusValidator(),
        UniqueUpdateDBValidator()
    ]


class OrderDetailRetrieveSerializer(serializers.ModelSerializer):
    tractor = TractorSerializer()
    t_type = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = (
            'order', 
            'quantity',
            'price',
        )

    def get_size(self, obj):
        return obj.get_size_display()


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'full_name',
            'address1', 
            'address2',
            'city',
            'phone',
            'created',
            'updated',
            'total_paid',
            'order_key',
            'billing_status',
            'order_status'
        )

    def get_status(self, obj):
        return obj.get_status_display()


class OrderRetrieveSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    details = OrderDetailRetrieveSerializer(many=True, read_only=True)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'number',
            'customer',
            'status',
            'details'
        )

    def get_status(self, obj):
        return obj.get_status_display()


class OrderStatusRetrieveSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'status',
        )

    def get_status(self, obj):
        return obj.get_status_display()


class OrderStatusUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'id',
            'status',
        )