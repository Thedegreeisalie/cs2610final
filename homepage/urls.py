from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contact', views.contact, name='contact'),
    url(r'^index', views.index, name='index'),
    url(r'^portfolio', views.portfolio, name='portfolio'),
]