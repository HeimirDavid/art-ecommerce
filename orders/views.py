from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from checkout.models import Order


@permission_required('is_superuser')
def view_orders(request):
    """
    A view only accessable for the superuser.
    Here the admin of the site can see all the orders
    """
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders.html', context)


# View only accessable by superuser
@permission_required('is_superuser')
def view_single_order(request, pk):
    """
    1. Get the single order picked by admin.
    2. Get the associated cart with that order.
    3. Get the cart items from that cart.
    4. get the shipping address associated with the carts user.
    """
    order = get_object_or_404(Order, pk=pk)
    cart = order.cart
    items = cart.cartitem_set.all()
    shipping_address = order.shipping_address
    context = {
        'order': order,
        'cart': cart,
        'items': items,
        'shipping_address': shipping_address
        }
    return render(request, 'singleorder.html', context)


@login_required
def user_orders(request):
    current_user = request.user

    user_orders = Order.objects.filter(user=current_user)
    order_list = list(user_orders.values())
    if not order_list:
        messages.error(
            request,
            "You don't have any orders yet. Please keep shopping")
        return redirect(reverse('index'))

    context = {
        'user_orders': user_orders,
    }
    return render(request, "userorders.html", context)
