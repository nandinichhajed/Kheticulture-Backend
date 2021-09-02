from django.urls import path 
from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    path('createorder/', views.CreateOrder, name = 'createorder'),
    #path('pyconfirmation/', views.payment_confirmation, name = 'payment_confirmation'),
    #path('userorders/', views.user_orders, name = 'user_orders'),
]