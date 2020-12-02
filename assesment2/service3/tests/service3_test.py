from flask import url_for
from flask_testing import TestCase

from app import app


class TestBase(TestCase):
    def create_app(self):
        return app


class TestNumber(TestBase):
    def test_number(self):
        response = self.client.get(url_for('affluence'))
        self.assertEquals(response.status_code,200)