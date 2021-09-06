from django.conf import settings
from django.db import models
from store.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order_user", null=True, blank=True)
    order_key = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country_code = models.CharField(max_length=4, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    payment_option = models.CharField(max_length=200, blank=True)
    billing_status = models.BooleanField(default=False)
    
    ORDER_PLACED = 'Order Placed'
    ACCEPTED = 'Order Accepted'
    TRANSIT = 'In Transit'
    DELIVERED = 'Delivered'

    ORDER_STATUSES = (
        (ORDER_PLACED, u'Order Placed'),
        (ACCEPTED, u'Order Accepted'),
        (TRANSIT, u'In Transit'),
        (DELIVERED, u'Delivered')
    )

    order_status = models.CharField(
        choices=ORDER_STATUSES,
        max_length=20,
        default=ORDER_PLACED
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

class OrderRating(models.Model):
    id = models.AutoField(primary_key=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    RATE_CHOICES = (
        (4, "excellent"),
        (3, "very good"),
        (2, "good"),
        (1, "bad"),
    )
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    review=models.TextField(verbose_name=("description"), help_text=("Not Required"), blank=True)

    def __str__(self):
        return str(self.id)