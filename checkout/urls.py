from django.conf.urls import url
from .views import checkout, orders

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^orders/$', orders, name='user_orders'),
]