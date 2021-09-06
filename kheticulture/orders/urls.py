from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('', CreateOrder.as_view()),
    path('orderstatus/<str:order_key>/', update_order_status, name='orderstatus'),
    path('paymentstatus/<str:order_key>/', update_payment_status, name='paymentstatus'),
    path('orderrating/', create_order_review, name = 'orderrating')
]