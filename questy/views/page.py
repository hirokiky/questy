from pyramid.view import view_config


@view_config(
    route_name='page',
    renderer='json',
    permission='view',
)
def detail_page():
    return {}
