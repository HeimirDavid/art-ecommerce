from django.conf.urls import url
from .views import view_cart, add_to_cart


urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^(?P<pk>\d+)/$', add_to_cart, name='add_to_cart'),
]
