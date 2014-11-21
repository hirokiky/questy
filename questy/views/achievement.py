from pyramid.view import view_config


@view_config(
    route_name='achievements',
    renderer='json',
    permission='view',
)
def list_achievements():
    return {}


@view_config(
    route_name='achievement',
    renderer='json',
    permission='view',
)
def detail_achievement():
    return {}
