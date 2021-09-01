from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer # this is the model that is being serialized
        fields = ('email','name','mobile','is_active','is_staff','created')
        