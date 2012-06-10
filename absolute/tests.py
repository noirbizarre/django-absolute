import os
import re
import json

from django.conf import global_settings
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.utils import override_settings


@override_settings(
    TEMPLATE_DIRS=(
        os.path.join(os.path.dirname(__file__), 'templates'),
    ),
    TEMPLATE_CONTEXT_PROCESSORS=global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
        'absolute.context_processors.absolute',
    ),
)
class AbsoluteTest(TestCase):
    urls = 'absolute.urls'

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
        data = json.loads(response.content)

        self.assertEqual(data['absolute'], 'http://testserver/test_context')
        domain = Site.objects.get_current().domain
        self.assertEqual(data['site'], 'http://%s/test_context' % domain)
