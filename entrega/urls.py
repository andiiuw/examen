from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.principal_list, name='principal_list'),

    url(r'^sala/lista/$', views.sala_list, name='sala_list'),
    url(r'^sala/(?P<pk>[0-9]+)/$', views.sala_detail, name='sala_detail'),
    url(r'^sala/(?P<pk>\d+)/remove/$', views.sala_remove, name='sala_remove'),
    url(r'^sala/new/$', views.sala_new, name='sala_new'),
    url(r'^sala/(?P<pk>[0-9]+)/edit/$', views.sala_edit, name='sala_edit'),

    url(r'^pelicula/lista/$', views.pelicula_list, name='pelicula_list'),
    url(r'^pelicula/(?P<pk>[0-9]+)/$', views.pelicula_detail, name='pelicula_detail'),
    url(r'^pelicula/(?P<pk>\d+)/remove/$', views.pelicula_remove, name='pelicula_remove'),
    url(r'^pelicula/new/$', views.pelicula_new, name='pelicula_new'),
    url(r'^pelicula/(?P<pk>[0-9]+)/edit/$', views.pelicula_edit, name='pelicula_edit'),

    url(r'^paquete/$', views.paquete_list, name='paquete_list'),
    url(r'^paquete/(?P<pk>[0-9]+)/$', views.paquete_detail, name='paquete_detail'),
    url(r'^paquete/(?P<pk>\d+)/remove/$', views.paquete_remove, name='paquete_remove'),
    url(r'^paquete/new/$', views.paquete_new, name='paquete_new'),
    url(r'^paquete/(?P<pk>[0-9]+)/edit/$', views.paquete_edit, name='paquete_edit'),

    url(r'^ciudad/lista/$', views.ciudad_list, name='ciudad_list'),
    url(r'^ciudad/nueva/$', views.ciudad_nueva, name='ciudad_nueva'),
    url(r'^ciudad/(?P<pk>[0-9]+)/edit/$', views.ciudad_edit, name='ciudad_edit'),
    url(r'^ciudad/(?P<pk>\d+)/remove/$', views.ciudad_remove, name='ciudad_remove'),
   
]
