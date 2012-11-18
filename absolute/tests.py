import os
import re
import json

from django.conf import global_settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.template import Context, Template
from django.test import TestCase
from django.test.utils import override_settings


@override_settings(
    TEMPLATE_DIRS=(
        os.path.join(os.path.dirname(__file__), 'templates'),
    ),
    TEMPLATE_CONTEXT_PROCESSORS=global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'absolute.context_processors.absolute',
    )
)
class AbsoluteTest(TestCase):
    urls = 'absolute.test_urls'

    def test_context_processors(self):
        RX_ROOT = re.compile(r'^http(?:s)?://.*[^/]$')
        RX_ROOT_URL = re.compile(r'^http(?:s)?://.*/$')

        url = reverse('test_context')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        for var in ('ABSOLUTE_ROOT', 'ABSOLUTE_ROOT_URL', 'SITE_ROOT', 'SITE_ROOT_URL'):
            self.assertTrue(var in response.context)
            content = response.context[var]
            if var.endswith('_URL'):
                self.assertTrue(RX_ROOT_URL.match(content))
            else:
                self.assertTrue(RX_ROOT.match(content))

    def test_template_tags(self):
        url = reverse('test_tags')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('request' in response.context)

        domain = Site.objects.get_current().domain
        data = json.loads(response.content)

        self.assertEqual(data['absolute'], 'http://testserver/test_context')
        self.assertEqual(data['site'], 'http://%s/test_context' % domain)

    def test_template_tag_as_syntax(self):
        url = reverse('test_tags_as')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('request' in response.context)

        domain = Site.objects.get_current().domain
        data = json.loads(response.content)

        self.assertEqual(data['absolute'], 'http://testserver/test_context')
        self.assertEqual(data['site'], 'http://%s/test_context' % domain)

    def test_site_fallback(self):
        '''Should fallback on http protocol if request is missing'''
        t = Template('''
            {% load absolute %}
            site: "{% site test_tags %}"
            ''')
        rendered = t.render(Context())
        domain = Site.objects.get_current().domain
        self.failUnless('site: "http://%s/test_tags"' % domain in rendered)
