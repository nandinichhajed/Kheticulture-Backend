import uuid

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, name, password, **other_fields)

    def create_user(self, email, name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.name

class Address(models.Model):
    """
    Address
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=150)
    phone = models.CharField(_("Phone Number"), max_length=50)
    postcode = models.CharField(_("Postcode"), max_length=50)
    address_line = models.CharField(_("Address Line 1"), max_length=255)
    address_line2 = models.CharField(_("Address Line 2"), max_length=255)
    town_city = models.CharField(_("Town/City/State"), max_length=150)
    delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    default = models.BooleanField(_("Default"), default=False)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return "Address"
        
        
class Message(models.Model):

    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    description = models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    others=models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    message_txt = models.TextField(verbose_name=_("message_txt"), help_text=_("Required"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)
        
        
class User_Message(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="order_items", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)
    
    
class Offer_Category(models.Model):
    name=models.CharField(max_length=150,blank=False)
    description=models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)
    
class Offer(models.Model):
    discount_category=models.ForeignKey(Offer_Category, verbose_name=_("Offer_Category"), on_delete=models.CASCADE)
    name=models.CharField(max_length=150,blank=False)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    is_active=models.BooleanField(default=False)
    description=models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)
    
class Customer_Offer(models.Model):
    customer=models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)
    offer=models.ForeignKey(Offer, verbose_name=_("Offer"), on_delete=models.CASCADE)
    use_count= models.IntegerField()
    description=models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)
    
