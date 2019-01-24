from django import forms
from .models import Product

class itemForm(forms.ModelForm):
	class Meta:
		model= Product
		fields=['sizes',]
		widgets = {
			'sizes': forms.Select()
		}
