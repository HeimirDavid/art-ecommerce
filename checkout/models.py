from django.db import models
from django.contrib.auth.models import get_user_model
from cart.models import Cart

User = get_user_model()

# Create your models here.
STATUS_CHOICES = (
    ("Started", "Started"),
    ("Finished", "Finished")
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #address
    final_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    order_id = models.CharField(max_length=100, unique=True, default="123ABC")
    cart = models.ForeignKey(Cart)
    status = models.Charfield(max_length=100, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(auto_add_now=True, auto_now=False)
