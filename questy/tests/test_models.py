import unittest
import transaction

from pyramid import testing

from questy.models import DBSession


class TestAdventurer(unittest.TestCase):
    def setUp(self):
        from questy.testing import setup_db
        setup_db()

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test__followers(self):
        from questy.models import User
        with transaction.manager:
            DBSession.add(User())
