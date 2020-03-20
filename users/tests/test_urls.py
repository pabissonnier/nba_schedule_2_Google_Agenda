from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import profile, show_favs, player_detail, teams_detail, remove_calendar, mentions, contact


class TestUrls(SimpleTestCase):

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_show_favs_page_url_resolves(self):
        url = reverse('show_favs')
        self.assertEquals(resolve(url).func, show_favs)

    def test_player_detail_url_resolves(self):
        url = reverse('player-detail', args=[123])
        self.assertEquals(resolve(url).func, player_detail)

    def test_team_detail_page_url_resolves(self):
        url = reverse('detail', args=[12])
        self.assertEquals(resolve(url).func, teams_detail)

    def test_remove_calendar_page_url_resolves(self):
        url = reverse('remove-calendar')
        self.assertEquals(resolve(url).func, remove_calendar)

    def test_mentions_page_url_resolves(self):
        url = reverse('mentions')
        self.assertEquals(resolve(url).func, mentions)

    def test_contact_page_url_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)
