# coding: utf-8

from django.conf.urls import url
from . import views
from comment import views as comment_view

urlpatterns = [
    # TODO: url name 언더스코어 대시로 고치기
    url(r'^meetup/$', views.MeetupListView.as_view(), name='meetup_list'),

    url(r'^meetup/(?P<pk>[0-9]+)/$', views.meetup_detail, name='meetup_detail'),
    url(r'^meetup/(?P<pk>[0-9]+)/edit/$', views.MeetupFormView.as_view(), name='meetup_edit'),

    # url(r'^meetup/(?P<pk>\d+)/join/$', views.meetup_join, name='meetup_join'),
    url(r'^meetup/(?P<pk>\d+)/user/$', views.meetup_user, name='meetup_user'),
    url(r'^meetup/(?P<pk>\d+)/comment/$', comment_view.CommentView.as_view(), name='meetup_comment'),

    url(r'^meetup/new/$', views.MeetupFormView.as_view(), name='meetup_new'),
    # url(r'^meetup/join/(?P<pk>\d+)/$', views.meetup_join, name='meetup_join'),

    url(r'^meetup/?(?P<tag_id>.*)/(?P<tag_slug>.*)/', views.MeetupListView.as_view(), name='tagcanvas-list'),
]
