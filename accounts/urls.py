# coding: utf-8
from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$', 'accounts.views.signup', name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view( #정적인 페이지 보여줄때 씀. Generic View
        template_name='signup_ok.html'
    ), name='signup_ok'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login_url'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', { 'next_page': '/login/'}, name='logout'),
]