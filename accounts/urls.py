from django.conf.urls import url
from .views import logout_view, login_view, register_user


urlpatterns = [
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^login/$', login_view, name="login"),
    url(r'^register/$', register_user, name="register")
]
