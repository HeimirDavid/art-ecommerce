from django import forms
from .models import UserAddress


class MakePaymentForm(forms.Form):
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2040)]

    credit_card_number = forms.CharField(label='Credit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)




class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        widgets = {'address_type': forms.HiddenInput()}
        fields = ['full_name', 'address1', 'address2', 'city', 'country', 'postal_code', 'phone_number', 'address_type']


class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        widgets = {'address_type': forms.HiddenInput()}
        fields = ['full_name', 'address1', 'address2', 'city', 'country', 'postal_code', 'phone_number', 'address_type']
        




