from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'tractor'

urlpatterns = [
     path('shipmentstatus/<str:order>/', views.update_shipment_status , name='shipmentstatus'),
]

