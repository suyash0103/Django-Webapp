from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # url(r'^$', views.index, name='index'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/favourite/
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]