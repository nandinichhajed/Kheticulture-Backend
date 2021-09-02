from django.shortcuts import render
# from .serializers import 
from .models import Job, JobImage, JobImage
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.contrib.gis.measure import Distance  
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
