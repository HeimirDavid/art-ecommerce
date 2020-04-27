from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Cart
from products.models import PrintPainting, Product


def view_cart(request):
    try:
        cart_session_id = request.session['cart_id']
    except:
        cart_session_id = None
    if cart_session_id:
        cart = Cart.objects.get(id=cart_session_id)
        context = {"cart": cart}
    else:
        empty_message = "Your cart is empty, please keep shopping."
        context = {"empty": True, 'empty_message': empty_message}

    template = "cart.html"
    return render(request, template, context)


def update_cart(request, pk):
    request.session.set_expiry(300000)
    try:
        cart_session_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        cart_session_id = new_cart.id

    cart = Cart.objects.get(id=cart_session_id)

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
    