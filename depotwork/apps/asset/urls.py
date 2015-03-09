__author__ = 'LiR'

from django.conf.urls import url, patterns, include


urlpatterns = patterns('apps.asset.views',
                       url('^$', 'home', name='asset home'),

)