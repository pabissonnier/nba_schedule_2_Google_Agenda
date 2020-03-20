from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/index.html')

    def test_upload_page(self):
        response = self.client.get(reverse('upload'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/upload.html')
