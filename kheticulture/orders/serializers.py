from store.models import Product
from django.db.models import fields
from .models import Order, OrderItem, OrderRating, OrderStatus
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
        )
    def create(self, validated_data):
        return Order.objects.create(**validated_data)

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
    order_key = serializers.IntegerField
    total_paid =  serializers.DecimalField(max_digits=5, decimal_places=2)
    billing_status = serializers.BooleanField()

    class Meta:
        model = Order
        fields = ('order_key','total_paid','billing_status')

    def update(self, instance, validated_data):
            instance.billing_status = validated_data.get('billing_status')
            instance.save()
            return instance

class OrderStatusSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(max_length = 20)
    status_key = serializers.PrimaryKeyRelatedField(queryset = Order.objects.get('order_key'))

    class Meta:
        model = OrderStatus
        fields = ('status_key', 'order_status', 'order_created', 'order_updated')
    
    def update(self, instance, validated_data):
            instance.order_status = validated_data.get('order_status')
            instance.save()
            return instance


    