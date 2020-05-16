from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product, PrintPainting, CollectionCategory


# Create your views here.
def get_products(request):
    """
    Create a view that will return a list of Products
    and render them to the products.html template.
    If there is a coll_id the collection should be returned 
    and the products that belong to that collection
    """
    if request.method=="GET":
        try:
            collection = CollectionCategory.objects.get(pk=(request.GET['coll_id']))
            print(collection)
            products = collection.product_set.all()
            coll_description = True
        except:
            products = Product.objects.filter(upload_date__lte=timezone.now
                ()).order_by('-upload_date')
            coll_description = False
            collection = ''
    collections = CollectionCategory.objects.all().order_by('name')

    context = {
        'products': products,
        'collections': collections,
        'collection': collection,
        'coll_description': coll_description,
    }

    print(coll_description)

    return render(request, 'products.html', context)


def get_single_product(request, pk):
    """
    Create a view that returns a single product basaed on it's pk
    and render it to product.html, or 404 if product is not found
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', {'product': product})