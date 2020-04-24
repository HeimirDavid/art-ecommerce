from django.conf.urls import url
from .views import get_products


urlpatterns = [
    url(r'^$', get_products, name='get_products'),
]