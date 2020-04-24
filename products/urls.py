from django.conf.urls import url
from .views import get_products, get_single_product


urlpatterns = [
    url(r'^$', get_products, name='get_products'),
    url(r'^(?P<pk>\d+)/$', get_single_product, name='get_single_product'),
]
