from django.test import TestCase
from .views import index


class TestHomePageViews(TestCase):
    def test_get_home_page(self):
        """
        Test that the home page is returned
        when accessing the index view
        """
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home/index.html")
