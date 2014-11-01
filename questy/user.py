from questy.models import (
    DBSession,
    Page,
    Arrival,
    User,
    follow,
)


def following_stream(user):
    """ Page stream of following.
    This function returns list of pages which has been arrived
    by people who followed by the 'user'.
    """
    return DBSession.query(Page).\
        join(Arrival).\
        join(User).\
        join(follow,
             (follow.c.following_id == User.user_id) &
             (follow.c.follower_id == user.user_id)).all()
