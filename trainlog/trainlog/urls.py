from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trainlog.views.home', name='home'),
    url(r'^$', include('diary.urls')),
    url(r'^index/$', 'diary.views.index', name='index'),
    url(r'^user/(\S+)/w/(?P<week>\d+)/$', 'diary.views.weekly_view', name='weekly_view'),
    url(r'^user/(\S+)/', 'diary.views.user_view', name='user_view'),

    url(r'^admin/', include(admin.site.urls)),
)
