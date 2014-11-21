from pyramid.view import view_config


@view_config(
    route_name='comments',
    renderer='json',
    request_method='POST',
    permission='comment',
)
def comment(request):
    return {}


@view_config(
    route_name='comments',
    renderer='json',
    request_method='GET',
    permission='view',
)
def list_comments():
    return {}


@view_config(
    route_name='comment',
    renderer='json',
    permission='view',
)
def detail_comment():
    return {}


@view_config(
    route_name='upvote',
    renderer='json',
    request_method='POST',
    permission='upvote',
)
def upvote():
    return {}


@view_config(
    route_name='downvote',
    renderer='json',
    request_method='POST',
    permission='downvote',
)
def downvote():
    pass
