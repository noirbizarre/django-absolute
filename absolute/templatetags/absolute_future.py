# -*- coding: utf-8 -*-
from django import VERSION
from django.template import Library

register = Library()

if VERSION >= (1, 5):

    from .absolute import absolute, site

    register.tag(absolute)
    register.tag(site)

else:

    from django.templatetags.future import url
    from .absolute import AbsoluteUrlNode, SiteUrlNode

    @register.tag
    def absolute(parser, token):
        '''
        Returns a full absolute URL based on the request host.

        This template tag takes exactly the same paramters as url template tag.
        '''
        node = url(parser, token)
        view_name = str(node.view_name).strip('"\'')
        return AbsoluteUrlNode(
            view_name=view_name,
            args=node.args,
            kwargs=node.kwargs,
            asvar=node.asvar
        )

    @register.tag
    def site(parser, token):
        '''
        Returns a full absolute URL based on the current site.

        This template tag takes exactly the same paramters as url template tag.
        '''
        node = url(parser, token)
        view_name = str(node.view_name).strip('"\'')
        return SiteUrlNode(
            view_name=view_name,
            args=node.args,
            kwargs=node.kwargs,
            asvar=node.asvar
        )
