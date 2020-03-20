from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mainapp.views import index, upload_page


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_upload_page_url_resolves(self):
        url = reverse('upload')
        self.assertEquals(resolve(url).func, upload_page)
