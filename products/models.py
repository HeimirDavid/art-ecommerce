from django.db import models
from django.utils import timezone

class OriginalPainting(models.Model):
    stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=100)

    def __unicode__(self):
        return self.stock


class PrintPainting(models.Model):
    size = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __unicode__(self):
        return self.size


class CollectionCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = image = models.ImageField(upload_to="img", blank=False, null=False)
    original_painting = models.ForeignKey(OriginalPainting, on_delete=models.CASCADE, null=False)
    print_1 = models.ForeignKey(PrintPainting, on_delete=models.CASCADE, related_name="print_one", blank=True,null=True)
    print_2 = models.ForeignKey(PrintPainting, on_delete=models.CASCADE, related_name="print_two", blank=True,null=True)
    print_3 = models.ForeignKey(PrintPainting, on_delete=models.CASCADE, related_name="print_three", blank=True,null=True)
    collection = models.ForeignKey(CollectionCategory, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __unicode__(self):
        return self.name


