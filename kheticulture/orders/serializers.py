from . import models
from .models import Order
from .models import OrderItem
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(),
                                                  many=False)
    
    class Meta:
        model = Order # this is the model that is being serialized
        fields = ('user','full_name','total_paid',
                        'order_key','payment_option','billing_status','order_status')

class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(),
                                                  many=False)
    
    product = serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all(),
                                                  many=False)
        
    class Meta:
        model = Order # this is the model that is being serialized
        fields = ('order','product','price','quantity')