from django.shortcuts import render
from django.utils import timezone
from newsposts.models import NewsPost
from products.models import Product


# Create your views here.
def index(request):

    posts = NewsPost.objects.filter(published_date__lte=timezone.now
        ()).order_by('-published_date')

    products = Product.objects.filter(upload_date__lte=timezone.now
                ()).order_by('-upload_date')
    context = {'posts': posts, 'products': products}
    return render(request, 'index.html', context)


def contact_view(request):
    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')
