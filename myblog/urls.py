from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from account.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login,logout
from blog.views import blog_about,blog_home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls),name='admin'),
    url(r'^blog/',include('blog.urls')),
    url(r'^about/$',blog_about,name='blog_about'),
    url(r'^$',blog_home,name='blog_home'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns +=[
    url(r'^accounts/login/$',login,{'template_name':'login.html'},name='login'),
    url(r'^accounts/logout/$',logout,name='logout'),
]

from django.conf import settings 
if settings.DEBUG is False:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT,}),
    )
