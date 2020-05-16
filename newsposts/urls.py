from django.conf.urls import url
from .views import get_newsposts, news_detail

urlpatterns = [
    url(r'^$', get_newsposts, name='get_newsposts'),
    url(r'^(?P<pk>\d+)/$', news_detail, name='news_detail'),
]