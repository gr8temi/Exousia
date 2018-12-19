from django import forms
from .models import Order,Lga


class OrderCreateForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'state','lga']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['lga'].queryset = Lga.objects.all()