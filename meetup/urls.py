from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hocos/$', views.home, name='home'),
]