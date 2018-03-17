# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.test import TestCase
from django.conf import settings

import responses, json

def add_response(method='get', path='/', json={}, status=200):
    url = '{}{}'.format(settings.APPGURU_URL, path)
    method = getattr(responses, method.upper())
    responses.add(method, url, json=json, status=status)

class LoginGetTestCase(TestCase):

    def setUp(self):
        url = reverse('kong_login')
        self.result = self.client.get(url)

    def test_is_ok(self):
        status = self.result.status_code
        assert status == 200, 'Expected 200. Got: {}'.format(status)

class LoginTestCase(TestCase):

    def setUp(self):
        self.url = reverse('kong_login')

    # @responses.activate
    def test_login_with_email_pass(self):
        data = {
            "username": "christo@appointmentguru.co",
            "password": "testtest1234",
            "client_id": settings.KONG_CLIENT_ID,
            "client_secret": settings.KONG_CLIENT_SECRET,
        }
        add_response('post', '/api/auth/login/')
        result = self.client.post(self.url, json.dumps(data), content_type="application/json")
        print(result.json())

    # @responses.activate
    def test_login_with_phone_pass(self):
        data = {
            "phone_number": "+27637444423",
            "password": "testtest",
            "client_id": settings.KONG_CLIENT_ID,
            "client_secret": settings.KONG_CLIENT_SECRET,
        }
        add_response('post', '/api/auth/phone/token/')
        result = self.client.post(self.url, json.dumps(data), content_type="application/json")
        print(result.json())

    # @responses.activate
    def test_login_with_otp(self):
        data = {
            "phone_number": "+27832566533",
            "otp": "7367",
            "client_id": settings.KONG_CLIENT_ID,
            "client_secret": settings.KONG_CLIENT_SECRET,
        }
        add_response('post', '/api/auth/phone/otp/')
        result = self.client.post(self.url, json.dumps(data), content_type="application/json")
        print(result.json())
