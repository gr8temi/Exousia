from django.conf.urls import url,include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import Prodcat,product_detail
from cart.views import cart_add
# from django.contrib.auth import views as auth_views

urlpatterns = [	
	url(r'^categories/(?P<pk>\d+)/$',Prodcat, name='category'),
	url(r'^product/(?P<pk>\d+)/$',product_detail , name='detail'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 