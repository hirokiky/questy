from pyramid.view import view_config


@view_config(
    route_name='activities',
    renderer='json',
    permission='view',
)
def list_activities():
    return {
        'message': "OK",
        'activities': [
            {'type': 'arrival', 'url': '/api/pages/1'},
        ]
    }
