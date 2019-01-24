from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Enter your Firstname')
	last_name = forms.CharField(max_length=30, required=True, help_text='Enter your Lastname')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		User= get_user_model()
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

