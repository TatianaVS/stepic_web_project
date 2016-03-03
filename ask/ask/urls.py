from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'qa.views.test', name='home'),
    url(r'^login/', 'qa.views.test', name='home'),
    url(r'^signup/', 'qa.views.test', name='home'),
    url(r'^ask/', 'qa.views.test', name='home'),
    url(r'^popular/', 'qa.views.test', name='home'),
    url(r'^new/', 'qa.views.test', name='home'),
    url(r'^question/', include('qa.urls', namespace="qa")),

    url(r'^admin/', include(admin.site.urls)),
)
