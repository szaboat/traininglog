from django.test import TestCase
from django.test import Client


class AddPageTestCase(TestCase):
    def test_add_redirects(self):
        client = Client()
        response = client.get('/add/')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, 'http://testserver/admin/diary/entry/add/')
