from django.conf.urls.defaults import patterns
from diary.views import index

urlpatterns = patterns('',
    (r'^$', index),
)
