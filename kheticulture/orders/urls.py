from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('', CreateOrder.as_view()),
    path('paymentstatus/', UpdatePayment.as_view())
]