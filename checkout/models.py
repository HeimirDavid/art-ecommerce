from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from carts.models import Cart


User = get_user_model()

# Create your models here.


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    county = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return str(self.user.username)


STATUS_CHOICES = (
    ("Started", "Started"),
    ("Finished", "Finished")
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order_id = models.CharField(max_length=100, unique=True, default="123ABC")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="Started")
    #address
    final_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.order_id
