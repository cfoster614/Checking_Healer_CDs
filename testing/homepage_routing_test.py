from unittest import TestCase
from app import create_app
from config import Config

LOG = "https://www.warcraftlogs.com/reports/btCAvx2fPwRgNy8F"
BOSS = 2689
CODE = "btCAvx2fPwRgNy8F"

"""
We are basing all of the testing off of the same information.
The same log(code), the same boss, and the same spell.
"""

class HomepageTestCase(TestCase):
    """Make sure homepage routes properly."""
    def setUp(self):
        self.app = create_app(config_class=Config)
        self.client = self.app.test_client()
        
    def test_get_homepage_template(self):
        """Does the homepage template show up correctly?"""
        with self.client as client:
            response = client.get('/healers_home', follow_redirects=True)
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h3 class="title-box">Choose a boss</h3>', html)

    def test_post_redirect_and_result(self):
        """Check if the POST request redirects and shows the expected result."""
        with self.client as client:
            data = {
                'log-input': LOG,
                'boss-list': BOSS,
            }
            response = client.post('/healers_home', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

            redirected_html = response.get_data(as_text=True)
            self.assertIn('<h2 class="title-box">The Vigilant Steward, Zskarn</h2>', redirected_html)
    
    def test_empty_url_error_message(self):
        """If url input is empty, show error."""
        with self.client as client:
            data = {
                'log-input': '',
                'boss-list': BOSS,
            }
            error = '<div class="alert">Invalid log url.</div>'
            response = client.post('/healers_home', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            
            redirected_html = response.get_data(as_text=True)
            self.assertIn('<h3 class="title-box">Choose a boss</h3>', redirected_html) #Redirect to homepage.
            self.assertIn(error, redirected_html)
            
    def test_invalid_url_error(self):
        with self.client as client:
            """If url input is invalid, show error."""
            data = {
                'log-input': 'https://www.warcraftlogs.com/reports/btCAvx',
                'boss-list': BOSS,
            }
            error = '<div class="alert">Invalid log url.</div>'
            response = client.post('/healers_home', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            
            redirected_html = response.get_data(as_text=True)
            self.assertIn('<h3 class="title-box">Choose a boss</h3>', redirected_html) #Redirect to homepage.
            self.assertIn(error, redirected_html)
            