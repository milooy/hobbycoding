from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hoco/$', views.meetup_list, name='meetup_list'),
    url(r'^hoco/(?P<pk>[0-9]+)/$', views.meetup_detail, name='meetup_detail'),
    url(r'^hoco/new/$', views.meetup_new, name='meetup_new'),
    url(r'^hoco/(?P<pk>[0-9]+)/edit/$', views.meetup_edit, name='meetup_edit'),
]