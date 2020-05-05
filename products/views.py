from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product, PrintPainting, CollectionCategory


# Create your views here.
def get_products(request):
    """
    Create a view that will return a list of Products
    and render them to the products.html template
    """
    if request.method=="GET":
        try:
            #products = []
            #for filter in request.GET['coll_id']:
                #print(filter)
            collection = CollectionCategory.objects.get(pk=(request.GET['coll_id']))
            print(collection)
            products = collection.product_set.all()
            print("pop")
        except:
            products = Product.objects.filter(upload_date__lte=timezone.now
                ()).order_by('-upload_date')
    collections = CollectionCategory.objects.all()
    print(collections)
    context = {
        'products': products,
        'collections': collections
    }

    return render(request, 'products.html', context)


def get_single_product(request, pk):
    """
    Create a view that returns a single product basaed on it's pk
    and render it to product.html, or 404 if product is not found
    """
    # prints = get_object_or_404(PrintPainting, )
    #prints = PrintPainting.objects.filter(productPrint=pk)

    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})