from unittest import TestCase
from app import create_app
from config import Config

LOG = "https://www.warcraftlogs.com/reports/btCAvx2fPwRgNy8F"
BOSS = 2689

class ResultsTestCase(TestCase):
    """Make sure results page routes properly."""
    def setUp(self):
        self.app = create_app(config_class=Config)
        self.client = self.app.test_client()
        
    def test_get_results_template(self):
        """Check results template."""
        with self.client as client:
            response = client.get(f'/healers_home/report{BOSS}btCAvx2fPwRgNy8F', follow_redirects=True)
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h2 class="title-box">The Vigilant Steward, Zskarn</h2>', html)

    def test_post_redirect_and_result(self):
        """Check if the POST request redirects and shows the expected result."""
        with self.client as client:
            data = {
                'pull-list': 0,
                'spell_names': ['Rapture'],
            }
            response = client.post(f'/healers_home/report{BOSS}btCAvx2fPwRgNy8F', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_spell_error_invalid(self):
        """Make sure invalid spell returns error message."""
        with self.client as client:
            data = {
                'pull-list': 0,
                'spell_names': ['Raptu'],
            }
            error = '<p class="danger">Please insert at least one spell.</p>'
            response = client.post(f'/healers_home/report{BOSS}btCAvx2fPwRgNy8F', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            
            redirected_html = response.get_data(as_text=True)
            self.assertIn('<h2 class="title-box">The Vigilant Steward, Zskarn</h2>', redirected_html) #Redirect to results page.
            self.assertIn(error, redirected_html)
    
    def test_spell_error_empty(self):
        """Make sure invalid spell returns error message."""
        with self.client as client:
            data = {
                'pull-list': 0,
                'spell_names': [],
            }
            error = '<p class="danger">Please insert at least one spell.</p>'
            response = client.post(f'/healers_home/report{BOSS}btCAvx2fPwRgNy8F', data=data, follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            
            redirected_html = response.get_data(as_text=True)
            self.assertIn('<h2 class="title-box">The Vigilant Steward, Zskarn</h2>', redirected_html) #Redirect to results page.
            self.assertIn(error, redirected_html)
            
    def test_one_spell_one_empty(self):
        """One spell should be allowed to be sent, even if there are multiple inputs up."""
        with self.client as client:
            data = {
                'pull-list': 0,
                'spell_names': ['Rapture', ''],
            }
            response = client.post(f'/healers_home/report{BOSS}btCAvx2fPwRgNy8F', data=data)
            self.assertEqual(response.status_code, 200)
            
           