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
    except Product.DoesNotExist:
        pass
    except:
        pass
    
        # Get the items and their quantity from the form from the user
    product_var = []
    if request.method == "POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            print(key,val)
            try:
                printSize = PrintPainting.objects.get(id=val)
                print(printSize.size)
                product_var.append(printSize)
                
            except:
                pass

        cart_item = CartItem.objects.create(cart=cart, product=product)

        if int(qty) <= 0:
            cart_item.delete()
        else:
            if len(product_var) > 0:
                cart_item.print_variations.clear()
                for item in product_var:
                    cart_item.print_variations.add(item)
                cart_item.quantity = qty
                cart_item.save()

        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total_for_product = float(item.product.original_painting.price) * item.quantity
            new_total += line_total_for_product
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        
        return redirect(reverse('view_cart'))

    else: 
        return redirect(reverse('view_cart'))
    