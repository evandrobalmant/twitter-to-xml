from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'twittertoxml.principal.views.index'),
    url(r'^busca/$', 'twittertoxml.principal.views.busca'),
    # url(r'^twittertoxml/', include('twittertoxml.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root':'/var/www/twittertoxml/media/'}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
