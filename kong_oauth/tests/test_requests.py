from django.test import TestCase, Client
from django.urls import reverse

class ClassListViewEndpointTestCase(TestCase):

    def setUp(self, *args, **kwargs):
        pass

    def test_form_post_oauth(self):

        url = reverse('login')
        data = {
            "username": "joe",
            "password": "soap"
        }
        result = self.client.post(url, data)