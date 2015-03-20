# coding:utf-8
__author__ = 'lirui'

from django.conf.urls import url, include, patterns

urlpatterns = patterns('depotwork.core.views',
      url(r'^$', 'settings', name='settings'),
      url(r'^password/$', 'password', name='password'),
      url(r'^pic/$', 'update_avatar', name='save_uploaded_picture'),
      # url(r'^(?P<username>[^/]+)/$', 'depotwork.core.views.profile', name='profile'),
)