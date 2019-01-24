from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from django.views import generic
from .models import About
from django.contrib.auth import get_user_model
from .forms import SignUpForm
from home.views import Home
from Product.views import Prodcat
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
# from django.contrib.auth.models import User

# Create your views here.
class Home(generic.TemplateView):
	template_name= 'home/index.html'

class UserFormView(View):
	form_class= SignUpForm
	template_name='account/sign-up.html'

	def get(self, request):
		form=self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self,request, **kwargs):
		form=self.form_class(request.POST)
		if form.is_valid():
			user= form.save(commit=False)
			username=form.cleaned_data['username']
			password= form.cleaned_data['password1']
			email= form.cleaned_data['email']
			user.set_password(password)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your account.'
			message = render_to_string('account/acc_active_email.html', {            
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token':account_activation_token.make_token(user),
			})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage( 
						mail_subject, message, to=[to_email]
			)
			email.send()
			
			return render(request,template_name='account/send.html')

			# user = authenticate(username=username, password=password)
		else:
			return render(request, self.template_name, {'form':form},)

def activate(request, uidb64, token):
	User=get_user_model()
	try:
		uid = urlsafe_base64_decode(uidb64).decode()
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		# login(request, user)
		return redirect('login')
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid!')