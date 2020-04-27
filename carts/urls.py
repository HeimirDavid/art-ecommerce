from django.conf.urls import url
from .views import view_cart, update_cart


urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^(?P<pk>\d+)/$', update_cart, name='update_cart'),
]
