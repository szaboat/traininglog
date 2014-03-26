from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from diary.views import RedirectToAdmin

urlpatterns = patterns('',
    url(r'^$', include('diary.urls')),
    url(r'^index/$', 'diary.views.index', name='index'),
    url(r'^user/(\S+)/(?P<year>\d+)/(?P<week>\d+)/', 'diary.views.weekly_view', name='weekly_view'),
    url(r'^user/(\S+)/', 'diary.views.user_view', name='user_view'),
    url(r'^add/$', RedirectToAdmin.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
