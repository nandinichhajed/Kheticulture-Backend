from django.http.response import JsonResponse
from .serializers import OrderSerializer, OrderItemSerializer
from django.shortcuts import get_object_or_404, render
from tractor.models import Tractor
from .models import Order, OrderItem
from rest_framework.decorators import api_view
from django.contrib.gis.measure import Distance  
from django.contrib.gis.measure import Distance  
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.gis.geos import Point

def add(request):
    #basket = Basket(request)
    tractor=Tractor(request)
    if request.POST.get('action') == 'post':

        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(user_id=user_id, full_name='name', address1='add1',
                                address2='add2', total_paid=baskettotal, order_key=order_key)
            order_id = order.pk

            #for item in basket:
            OrderItem.objects.create(order_id=order_id, product=tractor, price='', quantity=1)

        response = JsonResponse({'success': 'Return something'})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
