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
                    quantity=item['quantity'],
                    size=item['sizes'],
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