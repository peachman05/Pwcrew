from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.signup,  name='signup'),
    url(r'^password/$', views.change_password, name='change_password'),
]