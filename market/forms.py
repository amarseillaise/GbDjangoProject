from django import forms
from .models import Customers


class CustomerChoiceForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customers.objects.all())
