import unittest
from django.urls import reverse
from django.test import Client
from .models import PushApplication
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_pushapplication(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["api_key"] = "api_key"
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_django_contrib_auth_models_user()
    return PushApplication.objects.create(**defaults)


class PushApplicationViewTest(unittest.TestCase):
    '''
    Tests for PushApplication
    '''
    def setUp(self):
        self.client = Client()

    def test_list_pushapplication(self):
        url = reverse('push_app_pushapplication_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_pushapplication(self):
        url = reverse('push_app_pushapplication_create')
        data = {
            "name": "name",
            "description": "description",
            "api_key": "api_key",
            "user": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_pushapplication(self):
        pushapplication = create_pushapplication()
        url = reverse('push_app_pushapplication_detail', args=[pushapplication.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_pushapplication(self):
        pushapplication = create_pushapplication()
        data = {
            "name": "name",
            "description": "description",
            "api_key": "api_key",
            "user": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('push_app_pushapplication_update', args=[pushapplication.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


