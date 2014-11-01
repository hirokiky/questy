from questy.models import (
    DBSession,
    Page,
    Arrival,
    Comment,
    User,
    follow,
)


def following_arrival_stream(user):
    """ Arrived page stream of following users.
    This function returns list of pages which has been arrived
    by people who followed by the 'user'.
    """
    return DBSession.query(Page).\
        join(Arrival).\
        join(User).\
        join(follow,
             (follow.c.following_id == User.user_id) &
             (follow.c.follower_id == user.user_id)).all()


def following_comment_stream(user):
    """ Commented page stream of following users.
    This function returns list of pages which has been commented
    by people who followed by the 'user'.
    """
    return DBSession.query(Page).\
        join(Comment).\
        join(User).\
        join(follow,
             (follow.c.following_id == User.user_id) &
             (follow.c.follower_id == user.user_id)).all()
