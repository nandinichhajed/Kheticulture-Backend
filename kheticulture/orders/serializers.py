from store.models import Product
from django.db.models import fields
from .models import Order, OrderItem
from rest_framework import serializers
from django.conf import settings

class OrderSerializer(serializers.ModelSerializer):
    order_key = serializers.IntegerField
    full_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)
    address1 = serializers.CharField(max_length=250)
    address2 = serializers.CharField(max_length=250)
    city = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100)
    postal_code = serializers.CharField(max_length=20)
    country_code = serializers.CharField(max_length=4)
    total_paid =  serializers.DecimalField(max_digits=5, decimal_places=2)
    order_status = serializers.CharField(max_length = 20)
    

    class Meta:
        model = Order
        fields = (
            'order_key',
            'full_name',
            'email',
            'address1',
            'address2',
            'city',
            'phone',
            'postal_code',
            'country_code',
            'total_paid',
            'order_status'
        )
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
            instance.order_status = validated_data.get('order_status')
            instance.save()
            return instance


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):

    items = serializers.PrimaryKeyRelatedField(queryset = Order.objects.all(),
                        many = False)
    order_items = serializers.PrimaryKeyRelatedField(queryset = Product.objects.all(),
    many = False)

    class Meta:
        model = OrderItem
        fields = (
            'items',
            'order_items',
            'price',
            'quantity'
        )

class OrderBillingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('order_key','billing_status')

    def update(self, instance, validated_data):
            instance.order_status = validated_data.get('billing_status')
            instance.save()
            return instance
    