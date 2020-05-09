from django.db import models
from django.utils import timezone

class OriginalPainting(models.Model):
    stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=100)

    def __str__(self):
        return str(self.stock)


class CollectionCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = image = models.ImageField(upload_to="img", blank=False, null=False)
    original_painting = models.ForeignKey(OriginalPainting, on_delete=models.CASCADE, null=False)
    collection = models.ForeignKey(CollectionCategory, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.name


class PrintPainting(models.Model):
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.PositiveIntegerField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.size


