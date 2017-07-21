# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, override_settings
from django.contrib.auth import get_user_model
import json
import responses

## responses:
def kong_login_success():
    responses.add(
        responses.POST,
        'https://kong:8443/test/oauth2/token',
        body=json.dumps({'refresh_token': 'rtoken', 'token_type': 'bearer', 'access_token': 'atoken', 'expires_in': 7200}),
        status=200,
        content_type='application/json'
    )


class OAuthTestCase(TestCase):

    def login(self, data):
        return self.client.post('/oauth2/token/', json.dumps(data), content_type="application/json")

    @override_settings(KONG_GATEWAY_URL='https://kong:8443')
    @responses.activate
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='admin', password='testtest1234')
        data = {
          "username": "admin",
          "password": "testtest1234",
          "client_id": "cliendid",
          "client_secret": "secret"
        }
        kong_login_success()
        self.result = self.login(data)

    def test_is_ok(self):
        assert self.result.status_code == 200

    @responses.activate # assert no response is made
    def test_invalid_login_returns_401(self):
        data = {
          "username": "foo",
          "password": "bar",
        }
        result = self.login(data)
        assert result.status_code == 401
