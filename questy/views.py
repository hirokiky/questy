import colander

from pyramid import security
from pyramid.security import remember, forget, authenticated_userid
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPBadRequest

from questy.schema import LoginSchema
from questy.security import validate_password


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
    request_method='POST',
    renderer='json',
)
def login(request):
    schema = LoginSchema()
    try:
        deserialized = schema.deserialize(request.POST)
    except colander.Invalid as e:
        return HTTPBadRequest(e)

    email = deserialized['email']
    password = deserialized['password']

    if not validate_password(email, password):
        return {'message': 'Failed Login'}

    headers = remember(request, email)
    return HTTPFound(request.route_path('top'), headers=headers)


@view_config(
    route_name='logout',
    renderer='json',
)
def logout(request):
    headers = forget(request)
    return HTTPFound(request.route_path('top'), headers=headers)
