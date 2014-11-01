from pyramid.view import view_config

from questy.models import (
    DBSession,
    Page,
    Arrival,
    User,
    follow,
)


@view_config(
    route_name='dashboard',
    renderer='templates/dashboard.mako'
)
def dashboard(request):
    user = request.User
    session = DBSession()
    session.query(Page).\
        join(Arrival, Arrival.page_id == Page.page_id).\
        join(User, (User.User_id == Arrival.User_id) and
                   (follow.c.foller_id == User.User_id) and
                   (follow.c.following_id == User.User_id))

    return {}
