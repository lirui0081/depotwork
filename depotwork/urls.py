from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^asset/$', include('depotwork.apps.asset.urls')),
                        )

urlpatterns += patterns('',
    url(r'^$', 'depotwork.core.views.home', name='home'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'core/cover.html'}, name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^signup/$', 'depotwork.auth.views.signup', name='signup'),
    url(r'^settings/$', 'depotwork.core.views.settings', name='settings'),
    url(r'^settings/picture/$', 'depotwork.core.views.picture', name='picture'),
    url(r'^settings/upload_picture/$', 'depotwork.core.views.upload_picture', name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', 'depotwork.core.views.save_uploaded_picture', name='save_uploaded_picture'),
    url(r'^settings/password/$', 'depotwork.core.views.password', name='password'),
    url(r'^network/$', 'depotwork.core.views.network', name='network'),
    url(r'^feeds/', include('depotwork.feeds.urls')),
    url(r'^questions/', include('depotwork.questions.urls')),
    url(r'^articles/', include('depotwork.articles.urls')),
    url(r'^messages/', include('depotwork.messages.urls')),
    url(r'^notifications/all', 'depotwork.activities.views.notifications', name='notifications'),
    url(r'^notifications/last/$', 'depotwork.activities.views.last_notifications', name='last_notifications'),
    url(r'^notifications/check/$', 'depotwork.activities.views.check_notifications', name='check_notifications'),
    url(r'^notification/read','depotwork.activities.views.make_notification_read', name='make_notification_read'),
    url(r'^search/$', 'depotwork.search.views.search', name='search'),
    url(r'^(?P<username>[^/]+)/$', 'depotwork.core.views.profile', name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )