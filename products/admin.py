from django.contrib import admin
from .models import Product, PrintPainting, OriginalPainting, CollectionCategory


admin.site.register(Product)
admin.site.register(PrintPainting)
admin.site.register(OriginalPainting)
admin.site.register(CollectionCategory)

# Register your models here.
