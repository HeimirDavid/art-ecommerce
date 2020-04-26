from django.shortcuts import get_object_or_404
from products.models import PrintPainting, OriginalPainting


def cart_contents(request):
    """
    Make sure that the content in the cart is availible when rendering every page
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        print = get_object_or_404(PrintPainting, pk=id)
        original = get_object_or_404(OriginalPainting, pk=id)
        total += (quantity * print.price) + (quantity * original.price)
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'original': original, 'print': print})

    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count}
    