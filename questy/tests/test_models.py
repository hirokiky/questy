import unittest
import transaction

from pyramid import testing

from questy.models import DBSession


class TestAdventurer(unittest.TestCase):
    def setUp(self):
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from questy.models import Base
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test__followers(self):
        from questy.models import Adventurer
        with transaction.manager:
            DBSession.add(Adventurer())
