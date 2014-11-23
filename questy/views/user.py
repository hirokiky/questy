from pyramid.view import view_config


@view_config(
    route_name='user',
    renderer='json',
    permission='view',
)
def detail_user(request):
    return {
        'message': "OK",
        'user': {
            'url': '/api/users/1',
            'name': 'hiroki',
            'email': 'hirokiky@gmail.com',
            'style': 'cacual',
            'icon_path': 'http://hirokiky.org/images/1.jpg',
            'bio': 'Hello guys',
            'user_url': 'http://hirokiky.org/',
            'location': 'Japan',
            'language': 'Japanese',
            'created_at': '2014-11-05T00:00:00+00:00'
        }
    }


@view_config(
    route_name='follow',
    renderer='json',
    permission='follow',
)
def follow(request):
    return {
        'message': "OK",
        'user': {
            'url': '/api/users/1',
        }
    }


@view_config(
    route_name='unfollow',
    renderer='json',
    permission='unfollow',
)
def unfollow(request):
    return {
        'message': "OK",
        'user': {
            'url': '/api/users/1',
        }
    }


@view_config(
    route_name='followers',
    renderer='json',
    permission='view',
)
def list_followers(request):
    return {
        'message': "OK",
        'users': [
            {'url': '/api/users/1'},
        ]
    }


@view_config(
    route_name='followings',
    renderer='json',
    permission='view',
)
def list_followings(request):
    return {
        'message': "OK",
        'users': [
            {'url': '/api/users/1'},
        ]
    }
