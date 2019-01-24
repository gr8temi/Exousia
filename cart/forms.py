from django import forms
from Product.models import Product, size

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 26) ]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    sizes =forms.ModelMultipleChoiceField(queryset=size.objects.all(), to_field_name='name')