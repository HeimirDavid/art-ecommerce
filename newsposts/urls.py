from django.conf.urls import url
from .views import get_newsposts, news_detail, create_or_edit_newspost

urlpatterns = [
    url(r'^$', get_newsposts, name='get_newsposts'),
    url(r'^(?P<pk>\d+)/$', news_detail, name='news_detail'),
    url(r'^new/$', create_or_edit_newspost, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_newspost, name='edit_post'),
]