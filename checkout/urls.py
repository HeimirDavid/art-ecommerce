from django.conf.urls import url
from .views import checkout, orders, get_shipping_and_billing

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^orders/$', orders, name='user_orders'),
    url(r'^address/$', get_shipping_and_billing, name='addresses'),

]


