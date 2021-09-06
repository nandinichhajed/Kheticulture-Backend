from django.contrib.gis.db import models
from orders.models import Order 
from django.contrib.gis.geos import Point
from django.utils.translation import gettext_lazy as _

class Shipment(models.Model):
    order=models.ForeignKey(Order,related_name='Order',on_delete=models.CASCADE)
    shipment_status=models.CharField(max_length=150,blank=False)
    shipment_date=models.DateTimeField()
    dispatch_mode=models.CharField(max_length=150,blank=True)
    delivery_status=models.CharField(max_length=150,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    description=models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)
        
class Shippment_Tracking(models.Model):
    shipment=models.ForeignKey(Shipment,related_name='Shipment',on_delete=models.CASCADE)
    curr_location = models.PointField(default=Point(0,0))
    curr_date_time=models.DateTimeField()
    description=models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    
    class Meta:
        ordering = ("-curr_date_time",)

    def __str__(self):
        return str(self.curr_location)
   

# Create your models here.
