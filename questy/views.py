from pyramid.view import view_config


@view_config(
    route_name='dashboard',
    renderer='templates/dashboard.mako'
)
def dashboard(request):
    return {}
