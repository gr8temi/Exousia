from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    # url(r'^created/$', views.created.as_view(), name='order_created'),
    url(r'^lga/$', views.loadLga, name='load_lga'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 