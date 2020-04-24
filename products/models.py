from django.db import models

class OriginalPainting(models.Model):
    stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=100)


class PrintPainting(models.Model):
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class CollectionCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = image = models.ImageField(upload_to="img", blank=False, null=False)
    original_painting = models.ForeignKey(OriginalPainting, on_delete=models.CASCADE, null=False)
    prints = models.ForeignKey(PrintPainting, on_delete=models.CASCADE, blank=True,null=True)
    collection = models.ForeignKey(CollectionCategory, on_delete=models.CASCADE)



