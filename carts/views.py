from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Cart, CartItem
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



def update_cart(request, pk, qty):
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


    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        print("Yeah")
    if qty == 0:
        cart_item.delete()
    else:
        cart_item.quantity = qty
        cart_item.save()


    
    """ if not cart_item in cart.items.all(): 
        cart.items.add(cart_item)
    else:
        cart.items.remove(cart_item) """

    new_total = 0.00

    for item in cart.cartitem_set.all():
        line_total_for_product = float(item.product.original_painting.price) * item.quantity
        new_total += line_total_for_product

    request.session['items_total'] = cart.cartitem_set.count()

    cart.total = new_total
    cart.save()

    return redirect(reverse('view_cart'))
    