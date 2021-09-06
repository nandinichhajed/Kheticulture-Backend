from django.shortcuts import render
from .serializers import TractorSerializer, TractorTypesSerializer
from .models import Tractor, Tractor_Types
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.contrib.gis.measure import Distance  
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,ParseError
from django.contrib.gis.geos import Point

@api_view(['GET', 'POST', 'DELETE'])
def all_tractors(request):
    if request.method == 'GET':
        tractor = Tractor.objects.all()
        all_serializer = TractorSerializer(tractor, many=True)
        return JsonResponse(all_serializer.data, safe=False)
    elif request.method == 'POST':
        types_data = JSONParser().parse(request)
        types_serializer = TractorSerializer(data=types_data)
        if types_serializer.is_valid():
            types_serializer.save()
            return JsonResponse(types_serializer.data, status=status.HTTP_200_OK) 
        return JsonResponse(types_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tractor_Types.objects.all().delete()
        return JsonResponse({'message': '{} Tractor Types were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

def add(request):
    if request.method == 'GET':
        data = Tractor.objects.all()
        serializer = TractorTypesSerializer(data)
        return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])     
def get_available_tractors_within_radius(request):
    if request.method == 'GET':
        #get tractors within a radious R from user location
        request_data = JSONParser().parse(request)
        lat=request_data['lat']
        lon=request_data['lon']
        radius=request_data['radius']
        point = Point(lon, lat)    
        tractors=Tractor.objects.filter(location__distance_lt=(point, Distance(km=radius)),is_available=True)
        tractors_serializer = TractorSerializer(tractors, many=True)
    return JsonResponse(tractors_serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_tractor_within_radius(request):
    radius = Tractor.objects.filter(Tractor.location)
    if not radius:
        return Response({"message": "User is not Available","success":False},status=status.HTTP_400_BAD_REQUEST)
    
    query_set = Tractor.gis.filter(location__dwithin= radius)
    serializer = TractorSerializer(data=query_set,many=True,context={'request': request})
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_tractor_details(request,id):
    try: 
        detail = Tractor.objects.get(pk=id) 
    except Tractor.DoesNotExist: 
        return JsonResponse({'message': 'The tractor does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        detail_serializer = TractorSerializer(detail) 
        return JsonResponse(detail_serializer.data) 

@api_view(['PUT'])
def update_tractor_availabilty(request, id, availabilty):
    data = JSONParser().parse(request, pk=id) 
    
    if request.method == 'PUT': 
        serializer = TractorSerializer(Tractor, data=data) 
        if availabilty != data:
            if serializer.is_valid(): 
                serializer.save() 
                return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_tractor_rating(request, id):
    pass