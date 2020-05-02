from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from carts.models import Cart
from .models import Order, UserAddress
from .forms import ShippingAddressForm, BillingAddressForm, MakePaymentForm
from .utils import id_generator
import stripe


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

stripe.api_key = settings.STRIPE_SECRET

@login_required
def checkout(request):
    if request.method=="POST":
        # Get the cart object that mathes with the current users session id
        try:
            cart_session_id = request.session['cart_id']
            cart = Cart.objects.get(id=cart_session_id)
        except:
            messages.error(request, "Your cart is empty, please keep shopping")
            return redirect(reverse('get_products')) 
        print(cart)

        #create an instance of an order and fill it's fields
        try:
            new_order = Order.objects.get(cart=cart)
        except Order.DoesNotExist:
            new_order = Order()
            new_order.cart = cart
            new_order.user = request.user
            new_order.order_id = id_generator()
            new_order.final_total = cart.total
            new_order.save()
        except:
            messages.error(request, "We were unable to create an order at this moment")
            return redirect(reverse('view_cart')) 


        #create two different objects with shipping and billing address.
        shipping_address_form = ShippingAddressForm(request.POST)
        billing_address_form = BillingAddressForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if shipping_address_form.is_valid() and billing_address_form.is_valid() and payment_form.is_valid():
            #assign the shipping address from the form to the new shipping address object
            new_shipping_address = shipping_address_form.save(commit=False)
            new_shipping_address.user = request.user
            new_shipping_address.address_type = "Shipping"
            new_shipping_address.save()
            
            #assign the billing address from the form to the new billing address object
            new_billing_address = billing_address_form.save(commit=False)
            new_billing_address.user = request.user
            new_billing_address.address_type = "Billing"
            new_billing_address.save()

            #assign the order object these two different addresses
            new_order.shipping_address = new_shipping_address
            new_order.billing_address = new_billing_address
            new_order.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(new_order.final_total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")
            
            if customer.paid:
                messages.success(request, "You have successfully paid")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment")
        
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take payment with that card!")

            



        if new_order.status == "Finished":
            #cart.delete()
            del request.session['cart_id']
            del request.session['items_total']

    #run credit card
    #
    else:
        new_shipping_address = ShippingAddressForm(initial={'address_type': 'Shipping'})
        new_billing_address = BillingAddressForm(initial={'address_type': 'Billing'})
        payment_form = MakePaymentForm()

    context = {
        'new_shipping_address': new_shipping_address,
        'new_billing_address': new_billing_address,
        'payment_form': payment_form,
        'publishable': settings.STRIPE_PUBLISHABLE,
        }
    return render(request, 'checkout.html', context)