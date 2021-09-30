from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ShipmentSerializer
from .models import Shipment, Shippment_Tracking

def create_shipment(request, order, shipping_status):
    pass

@api_view(['PUT',])
def update_shipment_status(request, order):
    try:
        key = Shipment.objects.get(order = order)
    except Shipment.DoesNotExist:
        key = None
    serializer = ShipmentSerializer(instance=key, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)