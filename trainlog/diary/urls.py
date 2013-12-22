from django.conf.urls import patterns
from diary.views import index, home

urlpatterns = patterns('',
    (r'^$', home),
)
