from django.shortcuts import render
from .serializers import TractorSerializer
from .models import Tractor
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


def all_tractors(request):
    tractors = Tractor.objects.all()
    return render(request, 'tractor/home.html', {'tractors': tractors})
	
def add(request):
    tractor = Tractor(request)
    if request.POST.get('action') == 'post':
		
        response = JsonResponse({'success': 'Return something'})
        return response

@api_view(['GET'])
def get_all_tractor_within_radius(request):
    radius = Tractor.objects.filter(Tractor.location)
    if not radius:
        return Response({"message": "User is not Available","success":False},status=status.HTTP_400_BAD_REQUEST)
    
    query_set = Tractor.gis.filter(location__dwithin= radius)
    serializer = TractorSerializer(data=query_set,many=True,context={'request': request})
    return JsonResponse(serializer.data)

@api_view(['GET'])
def get_available_tractors_within_radius(request):
    if (Tractor.is_available == True):
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
