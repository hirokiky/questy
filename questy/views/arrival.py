from pyramid.view import view_config


@view_config(
    route_name='arrivals',
    renderer='json',
    request_method='POST',
    permission='arrive',
)
def arrive(request):
    return {}


@view_config(
    route_name='arrivals',
    renderer='json',
    request_method='GET',
    permission='view',
)
def list_arrival():
    return {}
