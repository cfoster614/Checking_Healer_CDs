from unittest import TestCase
from app import create_app
from config import TestConfig
import json
from app.extensions import db
from app.models.logs_database import Spell

# db.create_all()
URL = "https://wow.zamimg.com/images/wow/icons/large/"

class SpellModelTestCase(TestCase):
    """Make sure models work properly."""

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

    def test_spell_model(self):
        """Does basic model work?"""
        with self.app.app_context():
            spell = Spell(
                spell_id=370960,
                name="Emerald Communion",
                icon="https://wow.zamimg.com/images/wow/icons/large/ability_evoker_green_01.jpg"
            )
            db.session.add(spell)
            db.session.commit()

        with self.client as client:
            #Check api for spells route.
            response = client.get('/api.healer_cds.com/spells')
            self.assertEqual(response.status_code, 200)
            
            #Parse the JSON response
            data = json.loads(response.get_data(as_text=True))
            
            self.assertIn('spells', data) #Check for spells key
            self.assertTrue(any(spell['name'] == 'Emerald Communion' for spell in data['spells'])) #Check for Emerald Communion in spell data.
            self.assertFalse(any(spell['name'] == 'Rapture' for spell in data['spells'])) #Rapture should not be in the spell data currently.
    
    def test_spell_model_method(self):
        """Method should add and commit spell to database."""
        with self.app.app_context():
             Spell.add_spell(spell_id=370960, name="Emerald Communion", icon=f"{URL}ability_evoker_green_01.jpg")

        with self.client as client:
            """Check api for spells route."""
            response = client.get('/api.healer_cds.com/spells')
            self.assertEqual(response.status_code, 200)
            
            #Parse the JSON response
            data = json.loads(response.get_data(as_text=True))
            
            self.assertIn('spells', data)
            self.assertTrue(any(spell['name'] == 'Emerald Communion' for spell in data['spells']))
            self.assertFalse(any(spell['name'] == 'Rapture' for spell in data['spells']))
    
    