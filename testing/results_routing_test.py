from unittest import TestCase
from app import create_app
from config import TestConfig
from app.extensions import db
from app.models.logs_database import Boss


LOG = "https://www.warcraftlogs.com/reports/btCAvx2fPwRgNy8F"
BOSS = 2689
URL = "https://wow.zamimg.com/images/wow/icons/large/"

class ResultsTestCase(TestCase):
    """Make sure results page routes properly."""
    def setUp(self):
        self.app = create_app(config_class=TestConfig)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            boss = Boss(boss_id=2689,
                        name="The Vigilant Steward, Zskarn",
                        icon=f"{URL}zskarn.jpg",
                        nickname="Zskarn")
            db.session.add(boss)
            db.session.commit()
            
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
        

           