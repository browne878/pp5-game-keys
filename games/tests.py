from django.test import TestCase


class TestGamesViews(TestCase):
    """ Tests the views in the games app """
    
    def test_get_games_page(self):
        """ Tests the games page loads correctly """
        
        page = self.client.get("/games/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "games/games.html")

