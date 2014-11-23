from pyramid.view import view_config


@view_config(
    route_name='achievements',
    renderer='json',
    permission='view',
)
def list_achievements(request):
    return {
        'message': "OK",
        'achievements': [
            {'url': '/api/achievements/1'}
        ]
    }


@view_config(
    route_name='achievement',
    renderer='json',
    permission='view',
)
def detail_achievement(request):
    return {
        'message': "OK",
        'achievement': [
            {'url': '/api/achievements/1',
             'achievement_id': 1,
             'name': 'achievement',
             'description': 'this is really easy achievement',
             'image_path': '/static/achievements/1.jpg',
             'pont': 3000,
             'created_at': '2014-11-05T00:00:00+00:00',
             'updated_at': '2014-11-05T00:00:00+00:00'}
        ]
    }
