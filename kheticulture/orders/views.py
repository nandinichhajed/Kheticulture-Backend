from .serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Order, OrderRating

class CreateOrder(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)

    def post(self, request):
        order = request.data
        serializer = OrderSerializer(data = order)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order '{}' created successfully".format(order_saved.order_key)})

@api_view(['PUT',])
def update_order_status(request, order_key):
    key = Order.objects.get(order_key = order_key)
    serializer = OrderStatusSerializer(instance=key, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT',])
def update_payment_status(request, order_key):
    key = Order.objects.get(order_key = order_key)
    serializer = OrderBillingSerializer(instance=key, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST',])
def create_order_review(request):
    rating = request.data
    serializer = OrderSerializer(data = rating)
    if serializer.is_valid(raise_exception=True):
        saved_rating = serializer.save()
        return Response({"success": "Tractor rating '{}' created successfully".format(saved_rating.order_key)})

class OrderHistory(APIView):

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-order_key')
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)

def get_booking_request(request, user):
    pass

def get_booking_details(request, order_key):
    pass

