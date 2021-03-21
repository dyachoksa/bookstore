import logging

from django import forms

from .models import ShippingAddress

logger = logging.getLogger(__name__)


class CardForm(forms.Form):
    card_name = forms.CharField(label="Name on card", max_length=50)
    exp_date = forms.CharField(label="Exp", max_length=5)
    cvv = forms.CharField(label="CVV", max_length=4, widget=forms.PasswordInput)

    def charge(self):
        logger.info("Attempt to charge a cart for %s", self.cleaned_data['card_name'])

        # do API call here, etc.


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ["country", "city", "address_line", "zip_code"]
