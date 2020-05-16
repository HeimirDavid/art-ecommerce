from django.db import models
from products.models import Product, PrintPainting


#https://www.youtube.com/watch?v=20HCDEwEdeo&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=22


class Cart(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    print_variations = models.ManyToManyField(PrintPainting, blank=True) 
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.product.name)
