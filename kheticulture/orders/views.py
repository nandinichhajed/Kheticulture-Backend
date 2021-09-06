from .serializers import OrderSerializer, OrderBillingSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from .models import Order, OrderItem

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

    def put(self,request, *args, **kwargs):
        pk = self.kwargs.get('order_key')
        saved_order = get_object_or_404(Order.objects.all(), pk = pk)
        data = request.data
        serializer = OrderSerializer(instance=saved_order, data = data, partial = True)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order status of order {} updated successfully".format(order_saved.order_key)})

class UpdatePayment(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderBillingSerializer(orders, many = True)
        return Response(serializer.data)


    def put(self, request, order_key):
        payment = get_object_or_404(Order.objects.all(), order_key = order_key)
        data = request.data
        serializer = OrderBillingSerializer(instance= payment, data = data)
        if serializer.is_valid(raise_exception=True):
            payment = serializer.save()
        return Response({"success": "Payment status of order {} updated successfully".format(payment.order_key)})

    

    