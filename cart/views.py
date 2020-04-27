from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """Render the carts content on cart.html"""
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """
    add a quantity of the specific product to the cart
    """
    
    quantity = int(request.POST.get('quantity'))
    print(quantity)
    print(id)

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))

