from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Cart
from products.models import PrintPainting, Product


def view_cart(request):

    cart = Cart.objects.all()[0]
    template = "cart.html"
    prints = PrintPainting.objects.all()
    context = {"cart": cart, "prints": prints}

    return render(request, template, context)


def update_cart(request, pk):
    cart = Cart.objects.all()[0]
    try: 
        product = Product.objects.get(pk=pk) 
    except Product.DoesNotExist:
        pass
    except:
        pass
    if not product in cart.products.all(): 
        cart.products.add(product)
    else:
        cart.products.remove(product)

    new_total = 0.00

    for item in cart.products.all():
        new_total += float(item.original_painting.price)

    cart.total = new_total
    cart.save()

    return redirect(reverse('view_cart'))
    