from django.conf.urls import patterns
from diary.views import home

urlpatterns = patterns('',
    (r'^$', home),
)
