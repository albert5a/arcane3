from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def test_home_page_is_available(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_links_to_registration(self):
        response = self.client.get(reverse("home"))

        self.assertContains(response, f'href="{reverse("cadastro")}"')
