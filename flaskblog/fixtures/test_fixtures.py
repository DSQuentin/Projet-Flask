import unittest

from flaskblog import app
from flaskblog.models import db, Author, Album, Genre

from flask_fixtures import FixturesMixin

class TestFoo(unittest.TestCase, FixturesMixin):
    fixtures = ['extraits.json']

    app = app
    db = db
    