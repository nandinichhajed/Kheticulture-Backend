from rest_framework import viewsets
from rest_framework import exceptions
from orders.models import Order, OrderItem
from orders.serializers import (OrderDetailCreateSerializer, 
                    OrderDetailRetrieveSerializer, 
                    OrderRetrieveSerializer, 
                    OrderCreateSerializer, 
                    OrderDetailUpdateSerializer,
                    OrderStatusRetrieveSerializer,
                    OrderStatusUpdateSerializer)


class CreateOrder(viewsets.ModelViewSet):
    
    queryset = Order.objects.all()
    filter_fields = ('id', 'number', 'customer', 'status')

    def get_serializer_class(self):
        method = self.request.method
        serializer_class = OrderRetrieveSerializer
        if method == 'POST':
            serializer_class = OrderCreateSerializer
        return serializer_class

    def perform_create(self, serializer):
        """
        We need to override this method to add order details after a order
        is placed. Also note that extra validation is added to ensure order
        details come in the json data.
        """
        details = self.request.data.get('details')

        if not details:
            raise exceptions.ValidationError({
                'details': 'Please provide details for this order'
            })

        order_details_serialized = OrderDetailCreateSerializer(
            data=details, many=True)

        order_details_serialized.is_valid(raise_exception=True)

        order = serializer.save()
        order_details_serialized.save(order=order)