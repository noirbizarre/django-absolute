from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'absolute.views.home', name='home'),
    # url(r'^absolute/', include('absolute.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^test_context$', TemplateView.as_view(template_name="absolute/test_context.html"), name='test_context'),
    url(r'^test_tags$', TemplateView.as_view(template_name="absolute/test_tags.html"), name='test_tags'),
    url(r'^test_tags_as$', TemplateView.as_view(template_name="absolute/test_tags_as.html"), name='test_tags_as'),
)
