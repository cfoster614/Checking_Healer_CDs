from unittest import TestCase
from app import create_app
from config import TestConfig
from flask import session

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
        self.app = create_app(config_class=TestConfig)
        self.client = self.app.test_client()
        
    def test_set_session_data(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['assignement_data'] = [{'name': 'Holy Word: Salvation', 'times': ['00:10'], 'icon': 'https://wow.zamimg.com/images/wow/icons/large/ability_priest_archangel.jpg'}, {'name': 'Divine Hymn', 'times': ['01:10'], 'icon': 'https://wow.zamimg.com/images/wow/icons/large/spell_holy_divinehymn.jpg'}]
            
            response = client.get(f'/healers_home/report{BOSS}_{CODE}/comparison{PULL_ID}')
            self.assertEqual(response.status_code, 200)   
    def test_get_comparison_template(self):
        """Does the comparison template show up correctly?"""
        with self.client as client:
            
            response = client.get(f'/healers_home/report{BOSS}_{CODE}/comparison{PULL_ID}')
            self.assertEqual(response.status_code, 200)
            
        
                    