from django.conf.urls import patterns, url
from blog.views import *
urlpatterns = patterns('',

    url(r'^index$', BlogIndex, name="blog_index"),
    url(r'^detail/(?P<blog_id>\d+)/$', blogDetail, name='blog_detail'),
    url(r'^tag/(?P<tag_id>\d+)/$', tag, name='blog_tag'),
    url(r'^detail/(?P<blog_id>\d+)/commentshow/$', blog_show_comment, name='showcomment'),
    url(r'^bugTalk/', bug_talk, name='bug_talk'),
    url(r'^bugSubmit/$', bug_submit, name='bug_submit'),
    url(r'^bugSubmitInline/$', bug_submit_inline, name='bug_submit_inline'),
    url(r'^comments_upload/$', comments_upload, name='comments_upload'),
    url(r'^jqtest/$', jqtest, name='jqtest'),
    url(r'^jqget/$', jqget, name='jqget'),
    url(r'^jqpost/$', jqpost, name='jqpost'),
    url(r'^jqform/$', jqform, name='jqform'),
    url(r'modal/$', test_modal, name='modal'),
)

