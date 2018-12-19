from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import categories, Product
from django.views import generic
from cart.forms import CartAddProductForm
# Create your views here.


def Prodcat(request, pk):
	template= 'Product/prodcat.html'
	category = get_object_or_404(categories, pk=pk)
	product = Product.objects.filter(categories=category)

	context = {
	'category': category,
	'product': product,
	}
	return render(request, template, context)


class DetailView(generic.DetailView):
	model = Product
	template_name = 'Product/product.html'

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'Product/product.html', context)
