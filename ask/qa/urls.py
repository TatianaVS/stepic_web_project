from django.conf.urls import patterns, url

from qa import views


urlpatterns = patterns('',
                       url(r'^$', views.test, name='home'),
                       url(r'(?P<q_id>[0-9]+)/$', views.qid, name='qid'),
)
