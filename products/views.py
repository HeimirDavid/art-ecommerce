from django.shortcuts import render
from django.utils import timezone
from .models import Product #, PrintPainting, OriginalPainting, CollectionCategory


# Create your views here.
def get_products(request):
    """
    Create a view that will return a list of Products
    and render them to the products.html template
    """
    products = Product.objects.filter(upload_date__lte=timezone.now
        ()).order_by('-upload_date')
    return render(request, 'products.html', {'products': products})