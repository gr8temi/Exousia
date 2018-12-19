from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from Product.models import Product,categories,brand

# Create your views here.
class Home(generic.TemplateView):
	template_name= 'home/index.html'
	context_object_name = 'name'
	queryset = Product.objects.all()

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['cate']= categories.objects.all()
		context['brand']= brand.objects.all()
		context['prod'] = self.queryset
		return context
