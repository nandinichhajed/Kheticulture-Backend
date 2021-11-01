from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import ShipmentSerializer
from .models import Shipment, Shippment_Tracking

class CreateShipment(APIView):

    def get(self, request):
        shipments = Shipment.objects.all()
        serializer = ShipmentSerializer(shipments, many = True)
        return Response(serializer.data)

    def post(self, request):
        shipment = request.data
        serializer = ShipmentSerializer(data = shipment)
        if serializer.is_valid():
            shipment_saved = serializer.save()
        return Response({"success": "Shipment created successfully"})

@api_view(['PUT',])
def update_shipment_status(request, order):
    key = Shipment.objects.get(order = order)
    serializer = ShipmentSerializer(instance=key, data=request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)