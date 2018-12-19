from django.shortcuts import render
from .models import OrderItem,Lga
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})
    
def loadLga(request):
	state_id = request.GET.get('state')
	lga = Lga.objects.filter(state_id=state_id).order_by('lga')
	return render(request, 'orders/lga.html', {'lga':lga})
# class Order(View):
# 	form_class=OrderCreateForm
# 	template= 'orders/order/create.html'
# 	def get(self, request):
# 		form=self.form_class(None)
# 		return render(request, self.template, {'form':form})

# 	def post(self,request):
# 		cart = Cart(request) 
# 		form = self.form_class(request.POST)
# 		order=None
# 		if form.is_valid():
# 			order.save()
# 			for item in cart:
# 				OrderItem.objects.create(
# 					order=order,
# 					product=item['product'],
# 					price=item['price'],
# 					quantity=item['quantity']
# 				)
# 			cart.clear()
# 		return render(request, 'orders/order/created.html', {'order': order})

# def order_create(request):
# 	cart = Cart(request)    	
# 	order=None
# 	if request.method == 'POST':
# 		form = OrderCreateForm(request.POST)
# 		if form.is_valid():
# 			order = form.save(commit=False)
# 			order.save()
# 			for item in cart:
# 				OrderItem.objects.create(
# 					order=order,
# 					product=item['product'],
# 					price=item['price'],
# 					quantity=item['quantity']
# 				)
# 			cart.clear()
# 		return render(request, 'orders/created.html', {'order': order})
# 	else:
# 		form = OrderCreateForm()
# 	return render(request, 'orders/create.html', {'form': form})