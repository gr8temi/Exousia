from django.conf.urls import url
from . import views
from orders.views import order_create
app_name = 'cart'

urlpatterns = [
	url(r'^$', views.cart_detail, name='cart_detail'),
	url(r'^add/(?P<id>\d+)/$', views.cart_add, name='cart_add'),
	url(r'^remove/(?P<id>\d+)/$', views.cart_remove, name='cart_remove'),
	url(r'^create/$',order_create, name='order_create'),
]