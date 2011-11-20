from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
import os

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'twitter-to-xml.principal.views.index'),
    url(r'^busca/$', 'twitter-to-xml.principal.views.busca'),
    url(r'^xml/$', 'twitter-to-xml.principal.views.gerar_xml'),
    # url(r'^twittertoxml/', include('twittertoxml.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root':os.path.join(settings.PROJECT_PATH, 'media')}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
