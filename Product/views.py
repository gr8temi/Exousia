from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import categories, Product,Gender,brand
from django.views import generic
from cart.forms import CartAddProductForm
from django.http import JsonResponse
import json
# Create your views here.


def Prodcat(request, pk):
	template= 'Product/prodcat.html'
	category = get_object_or_404(categories, pk=pk)
	gender = Gender.objects.all()
	product = Product.objects.filter(categories=category)

	context = {
	'category': category,
	'gender':gender,
	'product': product,
	}
	return render(request, template, context)

def cate(request,pk,cat):
	template= 'Product/gender.html'
	gender= Gender.objects.all()
	gens= get_object_or_404(Gender, pk=pk)
	category=get_object_or_404(categories, pk=cat)
	cat= categories.objects.all()
	product = Product.objects.filter(gender=gens, categories=category )
	
	context = {
	# 'category': category,
	'gens': gens,
	'gender':gender,
	'product': product,
	'cat': cat,
	'category':category,
	}
	return render(request, template, context)
	

def Brand(request, pk):
	template= 'Product/brand.html'
	brands = get_object_or_404(brand, pk=pk)
	product = Product.objects.filter(brand=brands)
	gender = Gender.objects.all()
	shoes = Product.objects.filter(brand=brands, categories__categories='Shoes')
	accessories = Product.objects.filter(brand=brands, categories__categories='Accessories')
	wears = Product.objects.filter(brand=brands, categories__categories='Wears')
	context = {
	'brands': brands,
	'product': product,
	'gender': gender,
	'wears' :wears, 
	'accessories': accessories,
	'shoes':shoes,
	}
	return render(request, template, context)

# def genderView(request, pk, gpk):
# 	template= 'Product/gender.html'
# 	gend = get_object_or_404(gender, pk=pk)
# 	category = get_object_or_404(categories, pk=gpk)
# 	product = Product.objects.filter(gender=gender).annotate(categories=category)

# 	context = {
# 	'gend': gend,
# 	'product': product,
# 	'category': category,
# 	}
# 	return render(request, template, context)

def GenderView(request, pk):
	template= 'Product/gender.html'
	# category = get_object_or_404(categories, pk=pk)
	gender= Gender.objects.all()
	gens= get_object_or_404(Gender, pk=pk)
	product = Product.objects.filter(gender=gens)
	cat=categories.objects.all()
	context = {
	# 'category': category,
	'gens': gens,
	'gender':gender,
	'product': product,
	'cat': cat,
	
	}
	return render(request, template, context)

def genderCatSort(request,cpk):
	cat_id = get_object_or_404(categories, pk=cpk)
	gend_id = request.GET.get('gender')
	produ = Product.objects.filter(categories=cat_id, gender__gender=gend_id).order_by('prodname')
	context={
		'produ':produ,
		'cat_id':cat_id,
	}
	return render(request, 'Product/catsort.html',context)

def images(request):
	img = request.GET.get('src')


def Catsort(request,gpk):
	template='Product/gender.html'
	category=get_object_or_404(categories, pk=pk)
	prods= Product.objects.filter(categories=category)

	context={
	'category':category,
	'prods':prods,
	}
	return render(request, template, context)

def FemaleView(request, pk):
	template= 'Product/gender.html'
	cat= categories.objects.all()
	category = get_object_or_404(categories, pk=pk)
	gen= gender.objects.get(gender="Female")	
	product = Product.objects.filter(gender__gender="Female", categories=category)

	context = {
	'category': category,
	'gen':gen,
	'product': product,
	'cat': cat,
	}
	return render(request, template, context)

class DetailView(generic.DetailView):
	model = Product
	template_name = 'Product/product.html'

def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	item = CartAddProductForm()
	gender = Gender.objects.all()
	context = {
		'product': product,
		'item': item,
		'gender': gender,
	}
	return render(request, 'Product/product.html', context)
