from pyramid import security
from pyramid.security import remember, forget, authenticated_userid
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(
    route_name='top',
    renderer='templates/dashboard.mako',
    effective_principals=(security.Authenticated,)
)
def dashboard(request):
    user_email = authenticated_userid(request)
    return {'user_email': user_email}


@view_config(
    route_name='top',
    renderer='templates/top.mako',
)
def top(request):
    return {}


@view_config(
    route_name='login',
    renderer='json',
)
def login(request):
    headers = remember(request, 'hirokiky@gmail.com')
    return HTTPFound(request.route_path('top'), headers=headers)


@view_config(
    route_name='logout',
    renderer='json',
)
def logout(request):
    headers = forget(request)
    return HTTPFound(request.route_path('top'), headers=headers)
