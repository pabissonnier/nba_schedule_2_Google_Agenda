from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_profile_page(self):
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_show_favs_page(self):
        response = self.client.get(reverse('show_favs'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/contact.html')

    def test_mentions_page(self):
        response = self.client.get(reverse('mentions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/mentions.html')
