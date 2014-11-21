from pyramid.view import view_config


@view_config(
    route_name='user',
    renderer='json',
    permission='view',
)
def detail_user():
    return {}


@view_config(
    route_name='follow',
    renderer='json',
    permission='follow',
)
def follow():
    return {}


@view_config(
    route_name='unfollow',
    renderer='json',
    permission='unfollow',
)
def unfollow():
    return {}


@view_config(
    route_name='followers',
    renderer='json',
    permission='view',
)
def list_followers():
    return {}


@view_config(
    route_name='followings',
    renderer='json',
    permission='view',
)
def list_followings():
    return {}
