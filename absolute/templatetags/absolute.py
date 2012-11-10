# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.template import Library
from django.template.defaulttags import URLNode, url

register = Library()


class AbsoluteUrlNode(URLNode):
    def render(self, context):
        path = super(AbsoluteUrlNode, self).render(context)
        request = context['request']
        return request.build_absolute_uri(path)


@register.tag
def absolute(parser, token):
    '''
    Returns a full absolute URL based on the request host.

    This template tag takes exactly the same paramters as url template tag.
    '''
    node = url(parser, token)
    return AbsoluteUrlNode(
        view_name=node.view_name,
        args=node.args,
        kwargs=node.kwargs,
        asvar=node.asvar
    )


class SiteUrlNode(URLNode):
    def render(self, context):
        path = super(SiteUrlNode, self).render(context)
        domain = Site.objects.get_current().domain
        if 'request' in context:
            request = context['request']
            protocol = 'https' if request.is_secure() else 'http'
        else:
            protocol = 'http'
        return "%s://%s%s" % (protocol, domain, path)


@register.tag
def site(parser, token):
    '''
    Returns a full absolute URL based on the current site.

    This template tag takes exactly the same paramters as url template tag.
    '''
    node = url(parser, token)
    return SiteUrlNode(
        view_name=node.view_name,
        args=node.args,
        kwargs=node.kwargs,
        asvar=node.asvar
    )
