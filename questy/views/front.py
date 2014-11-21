from pyramid import security
from pyramid.view import view_config


@view_config(
    route_name='top',
    renderer='questy:templates/dashboard.mako',
    effective_principals=(security.Authenticated,)
)
def dashboard(request):
    return {}


@view_config(
    route_name='top',
    renderer='questy:templates/top.mako',
)
def top(request):
    return {}
