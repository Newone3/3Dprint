from django.conf.urls import url
from django.contrib import admin
from posts import views

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^about/$',views.AboutView.as_view(),name='about'),
	url(r'^contact/$',views.ContactView.as_view(),name='contact'),
	url(r'^prices/$',views.PricesView.as_view(),name='prices'),
	url(r'^services/$',views.ServicesView.as_view(),name='services'),
	url(r'^team/$',views.TeamView.as_view(),name='team'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
