from unittest import TestCase
from app import create_app
from config import TestConfig
import json
from app.extensions import db
from app.models.logs_database import Boss

# db.create_all()
URL = "https://wow.zamimg.com/images/wow/icons/large/"

class BossModelTestCase(TestCase):
    """Make sure model works properly."""

    def setUp(self):
        # Set up the test app with TestConfig
        self.app = create_app(config_class=TestConfig)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_boss_model(self):
        """Does basic model work?"""
        with self.app.app_context():
            boss = Boss(boss_id=2688,
                        name="Kazzara, the Hellforged",
                        icon=f"{URL}kazzara.jpg",
                        nickname="Kazzara")
            db.session.add(boss)
            db.session.commit()

        with self.client as client:
            #Check api bosses route.
            response = client.get('/api.healer_cds.com/bosses')
            self.assertEqual(response.status_code, 200)
            
            #Parse the JSON response.
            data = json.loads(response.get_data(as_text=True))
            
            self.assertIn('bosses', data) #Check for bosses key.
            self.assertTrue(any(boss['name'] == 'Kazzara, the Hellforged' for boss in data['bosses'])) #Check for Kazzara in boss data.
            self.assertFalse(any(boss['name'] == 'The Forgotten Experiments' for boss in data['bosses'])) #Experiments should not be in boss data currently.
    
    def test_boss_model_method(self):
        """Method should add and commit boss to database."""
        with self.app.app_context():
            
            Boss.add_boss(boss_id=2688, name="Kazzara, the Hellforged", icon=f"{URL}kazzara.jpg", nickname="Kazzara")
            
        with self.client as client:
            """Check api for bosses route."""
            response = client.get('/api.healer_cds.com/bosses')
            self.assertEqual(response.status_code, 200)
            
            #Parse the JSON response
            data = json.loads(response.get_data(as_text=True))
            
            self.assertIn('bosses', data)
            self.assertTrue(any(boss['name'] == 'Kazzara, the Hellforged' for boss in data['bosses'])) 
            self.assertFalse(any(boss['name'] == 'The Forgotten Experiments' for boss in data['bosses'])) 
        