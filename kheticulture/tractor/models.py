from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.contrib.gis.geos import Point

class Tractor_Types(models.Model):
    id= models.AutoField(primary_key=True)
    uud= models.UUIDField(
         unique=True,
         default = uuid.uuid4,
         editable = False)
    name=models.CharField(max_length=50, blank=True)
    created = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name
                
class Tractor_Sub_Types_Activities(models.Model):
    id= models.AutoField(primary_key=True)
    uud= models.UUIDField(
         default = uuid.uuid4,
         unique=True,
         editable = False)
    tractor_type = models.ForeignKey(Tractor_Types, on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
              
class Tractor(models.Model):
    #tractor_id=models.BigIntegerField(primary_key=True)
    #id= models.AutoField(primary_key=True)     
    #tractor_type_id=models.BigIntegerField(null=False)
    name=models.CharField(max_length=15, blank=True)
    tractor_type = models.ForeignKey(Tractor_Types, on_delete=models.CASCADE)
    tractor_sub_type = models.ForeignKey(Tractor_Sub_Types_Activities, on_delete=models.CASCADE)
    owner_id=models.BigIntegerField(null=True)
    engine_power=models.CharField(max_length=15, blank=True)
    no_of_wheels=models.CharField(max_length=10, blank=True)
    location = models.PointField(srid=4326,default='SRID=3857;POINT(0.0 0.0)')
    price_perhour=models.FloatField()
    is_available= models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("Tractor")
        verbose_name_plural = _("Tractor")
        
    def __str__(self):
        return self.name    
  
class Attachments(models.Model):
    #id=models.BigIntegerField(primary_key=True,null=False)
    id= models.AutoField(primary_key=True)
    uuid= models.UUIDField(
         unique=True,
         default = uuid.uuid4,
         editable = False)
    name=models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name    
      
        
class Tractor_Attachments(models.Model):
    id=models.BigIntegerField(primary_key=True)
    #tractor_id=models.BigIntegerField(primary_key=True)
    tractor_id = models.ForeignKey(Tractor, on_delete=models.CASCADE)
    atach_id=models.ForeignKey(Attachments, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    




