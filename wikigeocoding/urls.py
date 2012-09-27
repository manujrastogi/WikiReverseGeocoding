from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikigeocoding.views.home', name='home'),
    url(r'^$', 'latlag.views.home', name='home_page'),
    url(r'^parse/', 'latlag.views.parse_url', name='parse_url_page'),
    #url(r'^map/', 'latlag.views.geo_map', name='geo_map'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
