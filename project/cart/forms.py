from django import forms
from django.forms import ModelForm
from .models import Item


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(label='', choices=PRODUCT_QUANTITY_CHOICES, coerce=int,
    widget=forms.Select(
        attrs={'class': 'form-control'}
        ))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class Quantity(ModelForm):
    class Meta:
        model = Item
        fields = ('quantity',)

