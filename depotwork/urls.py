from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^asset/$', include('depotwork.apps.asset.urls')),
                        )

urlpatterns += patterns('',
    url(r'^$', 'depotwork.core.views.home', name='home'),

    url(r'^login', 'depotwork.core.views.login', {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^signup/$', 'depotwork.auth.views.signup', name='signup'),
    url(r'^setting/', include('depotwork.core.urls')),

    url(r'^feeds/', include('depotwork.feeds.urls')),
    url(r'^questions/', include('depotwork.questions.urls')),
    url(r'^articles/', include('depotwork.articles.urls')),
    url(r'^messages/', include('depotwork.messages.urls')),

    url(r'^notifications/all', 'depotwork.activities.views.notifications', name='notifications'),
    url(r'^notifications/last/', 'depotwork.activities.views.last_notifications', name='last_notifications'),
    url(r'^notifications/check/$', 'depotwork.activities.views.check_notifications', name='check_notifications'),
    url(r'^notification/read','depotwork.activities.views.make_notification_read', name='make_notification_read'),

    url(r'^search/$', 'depotwork.search.views.search', name='search'),

    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )