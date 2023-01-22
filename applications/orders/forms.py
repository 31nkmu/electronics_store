from dateutil.parser import parse
from django import forms


# from django.forms import forms


class PaymentForm(forms.Form):
    expiry = forms.CharField()

    def clean_expiry(self):
        expiry_date = self.cleaned_data.get('expiry')
        date_object = parse(expiry_date, dayfirst=False)