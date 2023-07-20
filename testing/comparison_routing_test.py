from unittest import TestCase
from app import create_app
from config import Config

LOG = "https://www.warcraftlogs.com/reports/btCAvx2fPwRgNy8F"
BOSS = 2689
CODE = "btCAvx2fPwRgNy8F"
QUERY_PARAMETERS = {
                'spells': ['Rapture'],
                'timers': '[{"name": "Rapture", "times": [""], "icon": "https://wow.zamimg.com/images/wow/icons/large/spell_holy_rapture.jpg"}]'
            }
PULL_ID = 9

class ComparisonTestCase(TestCase):
    
    def setUp(self):
        self.app = create_app(config_class=Config)
        self.client = self.app.test_client()
        
    def test_get_comparison_template(self):
        """Does the comparison template show up correctly?"""
        with self.client as client:
            response = client.get(f'/healers_home/report/{BOSS}{CODE}/comparison{PULL_ID}', query_string=QUERY_PARAMETERS)
            self.assertEqual(response.status_code, 200)
            
            html = response.get_data(as_text=True)
            self.assertIn('<h2 class="title-box">Your Assignments</h2>', html) #h2 will always be here.
            self.assertIn('<img src="https://wow.zamimg.com/images/wow/icons/large/spell_holy_rapture.jpg">', html) #Check to make sure the image correctly matches the spell.
            
    
                    