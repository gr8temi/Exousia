from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from Product.models import Product
from .cart import Cart
from .forms import CartAddProductForm
# Create your views here.

@require_POST
def cart_add(request, id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=id)
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'], sizes=cd['sizes'] )
	else:
		return HttpResponse(form.errors) 

	return redirect('cart:cart_detail')
	# return HttpResponse(cd['sizes'])

def cart_remove(request, id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=id)
	cart.remove(product)
	return redirect('cart:cart_detail')


def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'sizes':item['sizes'], 'update': True})
	return render(request, 'cart/detail.html', {'cart': cart})
	