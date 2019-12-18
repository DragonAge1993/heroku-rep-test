from django.test import TestCase
from django.test import SimpleTestCase

class SimpleTest(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/pages/')
        self.assertEqual(response.status_code, 200)
    def test_about_page_status(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)
# Create your tests here.
