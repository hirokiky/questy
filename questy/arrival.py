""" Arrivalの流れに関するビジネスロジック
"""
import sqlalchemy as sa

from questy.models import (
    DBSession,
    Arrival,
    Comment,
    Page,
    User,
)

from questy.webpage import fetch_page


def create_arrival_and_or_page(user, url):
    page = DBSession.query(Page).filter(url=url).first()
    if page:
        return arrive_page(user, page), True
    else:
        return first_arrive_page(user, url), False


def first_arrive_page(user, url):
    page = fetch_page(url)
    DBSession.add(page)
    arrival = Arrival(page=page,
                      user=user)
    page.arrivals.add(arrival)
    return arrival


def arrive_page(user, page):
    arrival = Arrival(page=page,
                      user=user)
    page.arrivals.add(arrival)
    return arrival


def arrival_pages(user_id):
    """ Build query object for arrived pages by a user
    ordered by created_at.
    """
    return DBSession.query(Page).\
        join(Arrival).\
        join(User).\
        filter(User.user_id == user_id).\
        order_by(sa.desc(Page.created_at))


def leave_comment(user, page, body):
    comment = Comment(page=page, user=user, body=body)
    DBSession.add(comment)
    return comment
