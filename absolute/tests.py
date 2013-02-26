import json

from unittest import skipIf

from django import VERSION
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.template import Context, Template, RequestContext
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.utils import override_settings
from django.conf.urls import patterns, url

from absolute.context_processors import absolute


class AbsoluteContextProcessorTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_context_processors_absolute(self):
        request = self.factory.get('/')
        context = absolute(request)

        self.assertIn('ABSOLUTE_ROOT', context)
        self.assertIn('ABSOLUTE_ROOT_URL', context)
        self.assertEqual(context['ABSOLUTE_ROOT'], 'http://testserver')
        self.assertEqual(context['ABSOLUTE_ROOT_URL'], 'http://testserver/')

    @override_settings(INSTALLED_APPS=('django.contrib.sites', 'absolute'))
    def test_context_processors_site(self):
        request = self.factory.get('/')
        context = absolute(request)

        domain = Site.objects.get_current().domain

        self.assertIn('SITE_ROOT', context)
        self.assertIn('SITE_ROOT_URL', context)
        self.assertEqual(context['SITE_ROOT'], 'http://%s' % domain)
        self.assertEqual(context['SITE_ROOT_URL'], 'http://%s/' % domain)

    @override_settings(INSTALLED_APPS=('absolute'))
    def test_context_processors_site_not_installed(self):
        request = self.factory.get('/')
        context = absolute(request)

        self.assertNotIn('SITE_ROOT', context)
        self.assertNotIn('SITE_ROOT_URL', context)


class AbsoluteTestMixin(object):
    urls = patterns('',
        url(r'^test$', 'test', name='test_url')
    )

    def setUp(self):
        self.factory = RequestFactory()

    def test_template_tags(self):
        request = self.factory.get(reverse('test_url'))
        t = Template('''%(load)s
            {
                "absolute": "{%% absolute %(url)s %%}",
                "site": "{%% site %(url)s %%}"
            }
            ''' % self.params)

        rendered = t.render(RequestContext(request))
        domain = Site.objects.get_current().domain
        data = json.loads(rendered)

        self.assertEqual(data['absolute'], 'http://testserver/test')
        self.assertEqual(data['site'], 'http://%s/test' % domain)

    def test_template_tag_as_syntax(self):
        request = self.factory.get(reverse('test_url'))
        t = Template('''%(load)s
            {%% absolute %(url)s as absolute_url %%}
            {%% site %(url)s as site_url %%}
            {
                "absolute": "{{ absolute_url }}",
                "site": "{{ site_url }}"
            }
            ''' % (self.params)
        )
        rendered = t.render(RequestContext(request))
        domain = Site.objects.get_current().domain
        data = json.loads(rendered)

        self.assertEqual(data['absolute'], 'http://testserver/test')
        self.assertEqual(data['site'], 'http://%s/test' % domain)

    def test_site_fallback(self):
        '''Should fallback on http protocol if request is missing'''
        t = Template('''%(load)s
            {
                "site": "{%% site %(url)s %%}"
            }
            ''' % self.params)
        rendered = t.render(Context())
        domain = Site.objects.get_current().domain
        data = json.loads(rendered)
        self.assertEqual(data['site'], 'http://%s/test' % domain)


@skipIf(VERSION >= (1, 5), "Syntax not supported by Django 1.5+")
class AbsoluteOldTest(AbsoluteTestMixin, TestCase):
    params = {
        'load': '{% load absolute %}',
        'url': 'test_url'
    }


@skipIf(VERSION < (1, 5), "Syntax only supported by Django 1.5+")
class AbsoluteNewTest(AbsoluteTestMixin, TestCase):
    params = {
        'load': '{% load absolute %}',
        'url': '"test_url"'
    }


class AbsoluteFutureTest(AbsoluteTestMixin, TestCase):
    params = {
        'load': '{% load absolute_future %}',
        'url': '"test_url"'
    }
