from pyramid.view import view_config


@view_config(
    route_name='page',
    renderer='json',
    permission='view',
)
def detail_page(request):
    return {
        'message': "OK",
        'page': {
            'url': '/api/pages/1',
            'page_id': 1,
            'page_url': 'http://hirokiky.org/',
            'title': 'hirokiky.org',
            'summary_image_url': 'http://hirokiky.org/images/1.jpg',
            'description': "This is Hiroki KIYOHARA's Web site",
            'created_at': '2014-11-05T00:00:00+00:00',
            'updated_at': '2014-11-05T00:00:00+00:00',
            'arrivals': [
                {'url': '/api/users/1'},
            ],
            'comments': [
                {'url': '/api/comments/1'},
            ]
        }
    }
