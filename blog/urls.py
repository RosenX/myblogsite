from django.conf.urls import *

urlpatterns = patterns(
    'blog.views',
    url(r'bloglist/$','blog_list',name='bloglist'),
    url(r'bloglist/(?P<method>\d)/(?P<id>\d+)/$','blog_list',name='blog_filter'),
    url(r'^blog/(?P<id>\d+)/$', 'blog_show', name='detailblog'),
    url(r'bloglist/add/$','blog_add',name='blogadd'),
    url(r'blog/(?P<blogId>\d+)/edit','blog_edit',name='blogedit'),
    url(r'blog/(?P<blogId>\d+)/del','blog_del',name='blogdel'),
    url(r'^blog/(?P<id>\d+)/commentshow/$', 'blog_show_comment', name='showcomment'),
)

