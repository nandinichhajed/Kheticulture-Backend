from django.shortcuts import render
from .models import Job, JobImage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.parsers import JSONParser,ParseError

def create_job(APIView):
    def get(self, request):
        job = Job.objects.all()
        serializer = JobSerializer(Job, many = True)
        return JsonResponse(serializer.data)

    def post(self, request):
        job = request.data
        serializer = JobSerializer(data = job)
        if serializer.is_valid(raise_exception=True):
            job_saved = serializer.save()
        return JsonResponse({"success": "Job '{}' Done successfully".format(job_saved.order_key)})

def update_job(request):
    key = Job.objects.get(order_key = order_key)
    serializer = JobStatusSerializer(instance=key, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data)

def post_invoice(request):
    invoice = request.data
    serializer = JobSerializer(data = invoice)
    if serializer.is_valid(raise_exception=True):
        Total_Cost = serializer.save()
        return JsonResponse({"success": "Total cost of the order is '{}' rs".format(Total_Cost.order_key)})