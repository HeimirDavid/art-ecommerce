from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Cart, CartItem
from products.models import PrintPainting, Product


def view_cart(request):
    # Get the cart by matching the cart session with the cart object
    try:
        cart_session_id = request.session['cart_id']
    except:
        cart_session_id = None
    if cart_session_id:
        cart = Cart.objects.get(id=cart_session_id)
        new_total = 0.00

        cart_items = cart.cartitem_set.all()

        # Check if cart is empty. if so, try to delete the items_total
        # which is the badge displaying the number of items in the cart
        if not cart_items:
            try:
                del request.session['items_total']
            except:
                pass
            messages.error(request, "Your cart is empty, please keep shopping")
            return redirect(reverse('get_products'))

        # loop through the items in the cart, get their price nad quantity
        # to calculate the total of the cart.
        for item in cart_items:
            line_total_for_product = float(item.line_total) * item.quantity
            new_total += line_total_for_product
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()

        context = {"cart": cart}
    # if the cart_session is None, it's empty. Redirect with message
    else:
        messages.error(request, "Your cart is empty, please keep shopping")
        return redirect(reverse('get_products'))

    return render(request, "cart.html", context)


def remove_from_cart(request, pk):
    # Delete the cart_item
    cartitem = CartItem.objects.get(pk=pk)
    cartitem.delete()
    return redirect(reverse('view_cart'))


def clear_cart(request):
    # Clear the whole cart and remove the items total
    try:
        del request.session['cart_id']
        del request.session['items_total']
        messages.success(request, 'Removed cart')
        return redirect(reverse('index'))
    except:
        messages.error(request, "Unable to remove clear cart.")
        return redirect(reverse('view_cart'))


def add_to_cart(request, pk):
    request.session.set_expiry(300000)
    # Check/Try if an instance of a cart session already exists and matches,
    # Otherwise create a new instance, match it with the id of the cart
    # so it's unique for the current user.
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

    # Get the items and their quantity from the form from the user
    # If the value is qty there is a print of a painting that is processed
    # and handled differently from the original painting
    product_var = []
    if request.method == "POST":
        # get the wished quantity from the customer of a print
        try:
            qty = request.POST['qty']
        except:
            pass

        # first if block handles the original painting, second the prints
        for item in request.POST:
            cart_items = cart.cartitem_set.all()

            if item == "original":
                # Error handling to prevent the user from adding an original
                # painting more than once in their cart. first,
                # check if the item in the cart is a print. if the list is
                # empty, the item is an original painting and this original
                # painting in the cart should not match with the
                # current painting the user is trying to add.
                # if it matches, return with an error message to the customer.
                for item in cart_items:
                    list_of_prints_in_cart = list(
                        item.print_variations.values('id'))
                    if not list_of_prints_in_cart:
                        painting_id = item.product.original_painting.id

                        if painting_id == product.original_painting.id:
                            messages.error(
                                request,
                                "This painting is already in your cart.")
                            return redirect(reverse('view_cart'))

                # if the item passes the test, a new CartItem
                # is created and the original painting is
                # added to the cart
                cart_item = CartItem.objects.create(
                    cart=cart,
                    product=product)
                qty = int(1)
                cart_item.product = product
                cart_item.quantity = qty
                cart_item.line_total = product.original_painting.price
                cart_item.save()
                messages.success(request, "Painting added to your cart!")
                return redirect(reverse('view_cart'))

            if item == "size":
                # error handling if the form returned
                # from the user is missing quantity
                if qty == "":
                    messages.error(
                        request,
                        "Missing quantity for your item.")
                    return render(
                        request, "product.html",
                        {'product': product})

                key = item
                val = request.POST[key]
                try:
                    single_product = PrintPainting.objects.get(
                        product=product,
                        id=val)
                    price = single_product.price
                    product_var.append(single_product)
                except:
                    # error handling if the form returned
                    # from the user is missing size
                    messages.error(request, "Missing size for your print.")
                    return render(request, "product.html", {'product': product})

                # error handling if the quantity is greater
                # than the current stock of an item
                if int(qty) > single_product.stock:
                        messages.error(
                            request,
                            "We unfortunately don't have enough stock for your requested item.")
                        return render(
                            request, "product.html",
                            {'product': product})

                # Error handling to check if the customers
                # print is already in the cart.
                # if so prevent the user from putting it in the cart.
                # This is to prevent the customer from putting
                # more items in a cart than the current stock allows
                cart_items = cart.cartitem_set.all()
                for item in cart_items:
                    list_of_prints_in_cart = list(
                        item.print_variations.values('id'))

                    for print_id in list_of_prints_in_cart:
                        the_print = print_id.get('id')

                        if the_print == single_product.id:
                            messages.error(
                                request,
                                "You already have this print in your cart.")
                            return render(
                                request, "product.html",
                                {'product': product})

        # if the print passes all the tests,
        # add the print_variations to the cart_item,
        # give it a price, quantity and save.
        # Redirect to the cart with success message to the user.
        cart_item = CartItem.objects.create(cart=cart, product=product)
        if len(product_var) > 0:
            cart_item.print_variations.add(*product_var)
        cart_item.line_total = price
        cart_item.quantity = qty
        cart_item.save()
        messages.success(request, "Item added to your cart!")
        return redirect(reverse('view_cart'))
    messages.error(request, "Unable to add item to your cart..")
    return redirect(reverse('view_cart'))
