from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product, PrintPainting #, OriginalPainting, CollectionCategory


# Create your views here.
def get_products(request):
    """
    Create a view that will return a list of Products
    and render them to the products.html template
    """
    products = Product.objects.filter(upload_date__lte=timezone.now
        ()).order_by('-upload_date')
    return render(request, 'products.html', {'products': products})


def get_single_product(request, pk):
    """
    Create a view that returns a single product basaed on it's pk
    and render it to product.html, or 404 if product is not found
    """
    # prints = get_object_or_404(PrintPainting, )
    #prints = PrintPainting.objects.filter(productPrint=pk)

    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})