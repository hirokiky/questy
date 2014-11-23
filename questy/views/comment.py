from pyramid.view import view_config


@view_config(
    route_name='comments',
    renderer='json',
    request_method='POST',
    permission='comment',
)
def comment(request):
    return {
        'message': "OK",
        'comment': {
            'comment_id': 1,
            'page': '/api/pages/1',
            'user': '/api/users/1',
            'body': 'body',
            'created_at': '2014-11-05T00:00:00+00:00',
            'updated_at': '2014-11-05T00:00:00+00:00',
        }
    }


@view_config(
    route_name='comments',
    renderer='json',
    request_method='GET',
    permission='view',
)
def list_comments(request):
    return {
        'message': "OK",
        'comments': [
            {'url': '/api/comments/1'},
        ]
    }


@view_config(
    route_name='comment',
    renderer='json',
    permission='view',
)
def detail_comment(request):
    return {
        'message': "OK",
        'comment': {
            'comment_id': 1,
            'page': '/api/pages/1',
            'user': '/api/users/1',
            'body': 'body',
            'upvote_count': 20,
            'downvote_count': 10,
            'created_at': '2014-11-05T00:00:00+00:00',
            'updated_at': '2014-11-05T00:00:00+00:00',
        }
    }


@view_config(
    route_name='upvotes',
    renderer='json',
    request_method='POST',
    permission='upvote',
)
def upvote(request):
    return {
        'message': "OK",
        'comment': {
            'url': '/api/comments/1',
        }
    }


@view_config(
    route_name='downvotes',
    renderer='json',
    request_method='POST',
    permission='downvote',
)
def downvote(request):
    return {
        'message': "OK",
        'comment': {
            'url': '/api/comments/1',
        }
    }


@view_config(
    route_name='upvotes',
    renderer='json',
    request_method='GET',
    permission='view',
)
def list_upvotes(request):
    return {
        'message': "OK",
        'users': [
            {'url': '/api/users/1'},
        ]
    }


@view_config(
    route_name='downvotes',
    renderer='json',
    request_method='GET',
    permission='view',
)
def list_downvotes(request):
    return {
        'message': "OK",
        'users': [
            {'url': '/api/users/1'},
        ]
    }
