from rest_framework import serializers
from .models import Customer, Address, Message, User_Message, Offer, Customer_Offer
from . import models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer # this is the model that is being serialized
        fields = ('email','name','mobile','is_active','is_staff','created')

class AddressSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(),
                                                  many=False) 
    class Meta:
        model = Address # this is the model that is being serialized
        fields = ('full_name','customer','phone','postcode','address_line','address_line2','town_city', 'delivery_instructions','created_at','updated_at','default',)

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message # this is the model that is being serialized
        fields = ('title','description','others','message_txt','created','updated')

class UserMessageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User_Message.objects.all(),
                                                  many=False) 
    
    message = serializers.PrimaryKeyRelatedField(queryset=User_Message.objects.all(),
                                                  many=False) 

    class Meta:
        model = User_Message # this is the model that is being serialized
        fields = ('created','user','message') 

class OfferCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer_Category # this is the model that is being serialized
        fields = ('description','name','created') 

class OfferSerializer(serializers.ModelSerializer):
    message = serializers.PrimaryKeyRelatedField(queryset=Offer.objects.all(),
                                                  many=False)
    class Meta:
        discount_category = Offer # this is the model that is being serialized
        fields = ('description','name','start_date','end_date','is_active','created',' discount_category')


class CustomerOfferSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer_Offer.objects.all(),
                                                  many=False) 
    
    offer = serializers.PrimaryKeyRelatedField(queryset=Customer_Offer.objects.all(),
                                                  many=False) 

    class Meta:
        model = Customer_Offer # this is the model that is being serialized
        fields = ('created','customer','offer','use_count','description') 

            