from django.conf.urls import url
from .views import view_orders, view_single_order


urlpatterns = [
    url(r'^$', view_orders, name='view_orders'),
    url(r'^order/(?P<pk>\d+)/$', view_single_order, name='order'),
]
