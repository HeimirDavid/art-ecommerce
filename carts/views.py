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
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total_for_product = float(item.product.original_painting.price) * item.quantity          
            new_total += line_total_for_product
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {"cart": cart}
    else:
        empty_message = "Your cart is empty, please keep shopping."
        context = {"empty": True, 'empty_message': empty_message}

    template = "cart.html"
    
    return render(request, template, context)


def remove_from_cart(request, pk):
    try:
        cart_session_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_session_id)
    except:
        return redirect(reverse('view_cart'))
    cartitem = CartItem.objects.get(pk=pk)
    print(cartitem)
    cartitem.cart = None
    cartitem.save()
    # Send message that it's deleted
    return redirect(reverse('view_cart'))



def add_to_cart(request, pk):
    request.session.set_expiry(300000)

    # Get the cart
    try:
        cart_session_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        cart_session_id = new_cart.id

    cart = Cart.objects.get(id=cart_session_id)

    # get the product
    try: 
        product = Product.objects.get(pk=pk)
        product_prints = PrintPainting.objects.get(pk=pk)
        print(product_prints)
    except Product.DoesNotExist:
        pass
    except:
        pass


    
    # Get the items and their quantity from the form from the user
    product_var = []
    if request.method == "POST":
        qty = request.POST['qty']

        for item in request.POST:
            if item == "size":
                print(item)
                key = item
                val = request.POST[key]
                print(item)
                try:
                    printSize = PrintPainting.objects.get(product=product, id=val)
                    product_var.append(printSize)
                except:
                    pass

        cart_item = CartItem.objects.create(cart=cart, product=product)
        
        if len(product_var) > 0:
            cart_item.print_variations.add(*product_var)
        cart_item.quantity = qty
        cart_item.save()
        # Success message
        return redirect(reverse('view_cart'))
    # Error message
    return redirect(reverse('view_cart'))
    