from django.conf.urls import url
from . import views

urlpatterns = [
    # TODO: url name 언더스코어 대시로 고치기
    url(r'^hoco/$', views.meetup_list, name='meetup_list'),
    url(r'^hoco/(?P<pk>[0-9]+)/$', views.meetup_detail, name='meetup_detail'),
    url(r'^hoco/new/$', views.meetup_new, name='meetup_new'),
    url(r'^hoco/(?P<pk>[0-9]+)/edit/$', views.meetup_edit, name='meetup_edit'),

    url(r'^hoco/join/(?P<pk>\d+)/$',
        views.meetup_join,
        name='meetup-join'),
]