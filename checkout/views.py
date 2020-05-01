from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from carts.models import Cart
from .models import Order, UserAddress
from .forms import AddressOrderForm
from .utils import id_generator



def orders(request):

    context = {}
    return render(request, "userorder.html", context)



@login_required
def get_shipping_and_billing(request):
    if request.method=="POST":
        address_form = AddressOrderForm(request.POST)
        all_shipping_addresses = UserAddress.objects.filter(user=request.user, address_type="Shipping")
        all_billing_addresses = UserAddress.objects.filter(user=request.user, address_type="Billing")
        if address_form.is_valid():
            new_order_address = address_form.save(commit=False)
            new_order_address.user = request.user
            new_order_address.save()
            

            is_shipping = request.POST.get('Shipping', False)
            if is_shipping:
                new_order_address.address_type = "Shipping"
                new_order_address.save()
            elif not is_shipping:
                print("BILLINNNNGGG")
                new_order_address.address_type = "Billing"
                new_order_address.save()
            else:
                print("Dafuq")

    else:
        new_order_address = AddressOrderForm()
        all_shipping_addresses = UserAddress.objects.filter(user=request.user, address_type="Shipping")
        all_billing_addresses = UserAddress.objects.filter(user=request.user, address_type="Billing")


    context = {
        'new_order_address': new_order_address,
        'all_shipping_addresses': all_shipping_addresses,
        'all_billing_addresses': all_billing_addresses
    }
    return render(request, 'addresses.html', context)


@login_required
def checkout(request):
    if request.method=="POST":
        try:
            cart_session_id = request.session['cart_id']
            cart = Cart.objects.get(id=cart_session_id)
        except:
            messages.error(request, "Your cart is empty, please keep shopping")
            return redirect(reverse('get_products')) 
        print(cart)


        try:
            new_order = Order.objects.get(cart=cart)
        except Order.DoesNotExist:
            new_order = Order()
            new_order.cart = cart
            new_order.user = request.user
            new_order.order_id = id_generator()
            new_order.save()
        except:
            messages.error(request, "We were unable to create an order at this moment")
            return redirect(reverse('view_cart')) 



        """
        address_form = AddressOrderForm(request.POST)
        print(address_form)
        if address_form.is_valid():
            new_order_address = address_form.save(commit=False)
            new_order_address.user = request.user
            new_order_address.save()"""
        

        


        if new_order.status == "Finished":
            #cart.delete()
            del request.session['cart_id']
            del request.session['items_total']

    #run credit card
    else:
        new_order_address = AddressOrderForm()

    context = {'new_order_address': new_order_address}
    return render(request, 'checkout.html', context)