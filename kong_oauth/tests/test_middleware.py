from django.test import TestCase, override_settings, Client
from django.core.urlresolvers import reverse

class KongDownstreamingTestCase(TestCase):

    def test_headers_log_you_in(self):
        headers = {
            'HTTP_ACCEPT': 'text/html',
            'HTTP_X_ANONYMOUS_CONSUMER': 'false',
            'HTTP_X_AUTHENTICATED_USERID': '1',
            'HTTP_X_CONSUMER_USERNAME': 'jimminy-the-cricket'
        }
        result = self.client.get('/', **headers)
