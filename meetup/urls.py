from django.conf.urls import url, include
from . import views
# from taggit_templatetags2 import urls as taggit_templatetags2_urls
from taggit_templatetags2 import urls as taggit_templatetags2_urls

urlpatterns = [
    # TODO: url name 언더스코어 대시로 고치기
    url(r'^meetup/$', views.MeetupListView.as_view(), name='meetup_list'),
    url(r'^meetup/(?P<pk>[0-9]+)/$', views.meetup_detail, name='meetup_detail'),
    # url(r'^meetup/new/$', views.meetup_new, name='meetup_new'),
    url(r'^meetup/new/$', views.MeetupFormView.as_view(), name='meetup_new'),
    # url(r'^meetup/(?P<pk>[0-9]+)/edit/$', views.meetup_edit, name='meetup_edit'),
    url(r'^meetup/(?P<pk>[0-9]+)/edit/$', views.MeetupFormView.as_view(), name='meetup_edit'),

    url(r'^meetup/join/(?P<pk>\d+)/$', views.meetup_join, name='meetup_join'),
    url(r'^meetup/(?P<pk>\d+)/like/$', views.meetup_like, name='meetup_like'),

    # url(r'^tags/', include(taggit_templatetags2_urls)),
    url(r'^meetup/?(?P<tag_id>.*)/(?P<tag_slug>.*)/',
        views.MeetupListView.as_view(), name='tagcanvas-list'),
    # url(r'^tag-list/(?P<tag_id>.*)/(?P<tag_slug>.*)/',
    #     TagCanvasListView.as_view(), name='tagcanvas-list'),
]
