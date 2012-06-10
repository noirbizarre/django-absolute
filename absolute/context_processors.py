# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site


def get_site_url(request, slash=False):
    domain = Site.objects.get_current().domain
    protocol = 'https' if request.is_secure() else 'http'
    root = "%s://%s" % (protocol, domain)
    if slash:
        root += '/'
    return root


def absolute(request):
    return {
        'ABSOLUTE_ROOT': request.build_absolute_uri('/')[:-1],
        'ABSOLUTE_ROOT_URL': request.build_absolute_uri('/'),
        'SITE_ROOT': get_site_url(request),
        'SITE_ROOT_URL': get_site_url(request, True),
    }
