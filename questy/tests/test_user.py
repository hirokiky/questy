import unittest

from pyramid import testing

from questy.models import DBSession


class TestFollowingArrivalStream(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from questy.user import following_arrival_stream
        return following_arrival_stream(*args, **kwargs)

    def setUp(self):
        from questy.testing import setup_db
        setup_db()

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test__following_arrived(self):
        from questy.models import User, Arrival, Page
        arrival = Arrival()
        follower = User(user_id=1)
        following = User(user_id=2)

        page = Page()
        page.arrivals = [arrival]
        follower.followings = [following]
        following.arrivals = [arrival]

        DBSession.add(arrival)
        DBSession.add(following)
        DBSession.add(follower)
        DBSession.add(page)

        actual = self._callFUT(follower)
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0].page_id, page.page_id)

    def test__another_user_arrived(self):
        from questy.models import User, Arrival, Page
        arrival = Arrival()
        user1 = User(user_id=1)
        user2 = User(user_id=2)

        page = Page(page_id=1)
        page.arrivals = [arrival]
        user2.arrivals = [arrival]

        DBSession.add(arrival)
        DBSession.add(user1)
        DBSession.add(user2)
        DBSession.add(page)

        actual = self._callFUT(user1)
        self.assertEqual(len(actual), 0)


class TestFollowingCommentStream(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from questy.user import following_comment_stream
        return following_comment_stream(*args, **kwargs)

    def setUp(self):
        from questy.testing import setup_db
        setup_db()

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test__following_commented(self):
        from questy.models import User, Comment, Page
        comment = Comment()
        follower = User(user_id=1)
        following = User(user_id=2)

        page = Page(page_id=1)
        page.comments = [comment]
        follower.followings = [following]
        following.comments = [comment]

        DBSession.add(comment)
        DBSession.add(following)
        DBSession.add(follower)
        DBSession.add(page)

        actual = self._callFUT(follower)
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0].page_id, page.page_id)

    def test__another_user_arrived(self):
        from questy.models import User, Comment, Page
        comment = Comment()
        user1 = User(user_id=1)
        user2 = User(user_id=2)

        page = Page(page_id=1)
        page.comments = [comment]
        user2.comments = [comment]

        DBSession.add(comment)
        DBSession.add(user1)
        DBSession.add(user2)
        DBSession.add(page)

        actual = self._callFUT(user1)
        self.assertEqual(len(actual), 0)
