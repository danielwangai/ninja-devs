"""
To set up tests
"""
import unittest


# local imports
from app import create_app
from app.models import db


class BaseTestCase(unittest.TestCase):
    def create_test_app(self):
        app = create_app("testing")
        return app

    def setUp(self):
        """
        Declare test-wide variables.
        """
        self.app = self.create_test_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
