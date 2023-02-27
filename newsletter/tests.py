from django.test import TestCase


class NewsletterViewsTestCase(TestCase):
    def test_newsletter_signup(self):
        """Tests the newsletter signup page loads correctly"""
        page = self.client.get("/newsletter/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "newsletter/newsletter.html")
