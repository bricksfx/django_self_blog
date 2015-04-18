from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^', include('blog.urls', namespace='blog')),
)
