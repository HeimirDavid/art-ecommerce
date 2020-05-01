import time
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from carts.models import Cart
from .models import Order
from .forms import AddressOrderForm

"""
# Create your views here.
#@login_required()
def checkout(request):
    
    try:
        cart_session_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_session_id)
    except:
        messages.error(request, "Your cart is empty, please keep shopping")
        return redirect(reverse('get_products'))        

    
    address_form = AddressOrderForm(request.POST or None)

    if address_form.is_valid():
        new_order_address = address_form.save(commit=False)
        new_order_address.user = request.user
        new_order_address.save()

    #print(cart, cart_session_id)
        context = {'new_order_address': new_order_address}
        return render(request, 'checkout.html', context)"""

def orders(request):

    context = {}
    return render(request, "userorder.html", context)


@login_required
def checkout(request):
    try:
        cart_session_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_session_id)
    except:
        messages.error(request, "Your cart is empty, please keep shopping")
        return redirect(reverse('get_products')) 
    print(cart)

    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        #assign a user to the order
        #assign address
        new_order.order_id = str(time.time())
        new_order.save()

    if new_order.status == "Finished":
        cart.delete()
        del request.session['cart_id']
        del request.session['items_total']

    #run credit card

    """
    address_form = AddressOrderForm(request.POST or None)
    if address_form.is_valid():
        
        form = address_form.save(commit=False)
        form.save()
    context = {'form': form}"""
    context = {}
    return render(request, 'checkout.html', context)