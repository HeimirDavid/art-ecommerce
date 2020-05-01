from django import forms
from .models import UserAddress

class AddressOrderForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['full_name', 'address1', 'address2', 'city', 'county', 'postal_code', 'phone_number']


