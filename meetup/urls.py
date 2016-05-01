from django.conf.urls import url
from . import views

urlpatterns = [
    # TODO: url name 언더스코어 대시로 고치기
    # url(r'^meetup/$', views.meetup_list, name='meetup_list'),
    url(r'^meetup/$', views.MeetupListView.as_view(), name='meetup_list'),
    url(r'^meetup/(?P<pk>[0-9]+)/$', views.meetup_detail, name='meetup_detail'),
    url(r'^meetup/new/$', views.meetup_new, name='meetup_new'),
    url(r'^meetup/search/$', views.meetup_filtered, name='meetup_filtered'),
    url(r'^meetup/(?P<pk>[0-9]+)/edit/$', views.meetup_edit, name='meetup_edit'),

    url(r'^meetup/join/(?P<pk>\d+)/$', views.meetup_join, name='meetup_join'),
    url(r'^meetup/(?P<pk>\d+)/like/$', views.meetup_like, name='meetup_like'),
]