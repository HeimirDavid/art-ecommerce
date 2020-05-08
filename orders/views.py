from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from checkout.models import Order

# Create your views here.
@permission_required('is_superuser')
def view_orders(request):

    orders = Order.objects.all()


    print(orders)
    context = {'orders': orders}
    return render(request, 'orders.html', context)

@permission_required('is_superuser')
def view_single_order(request, pk):
    """
    1. Get the single order picked by admin. check
    2. Get the associated cart with that order. check
    3. Get the cart items from that cart. check
    4. check for variations for that each cart-item.
    5. get the shipping address associated with the carts user.
    """
    order = get_object_or_404(Order, pk=pk)
    cart = order.cart
    items = cart.cartitem_set.all()
    shipping_address = order.shipping_address
    

    print(items)
    context = {
        'order': order,
        'cart': cart,
        'items': items,
        'shipping_address': shipping_address
        }
    return render(request, 'singleorder.html', context)


def user_orders(request):
    current_user = request.user
    user_orders = Order.objects.filter(user=current_user)

    print(user_orders)
    context = {
        'user_orders': user_orders,

    }
    return render(request, "userorders.html", context)
