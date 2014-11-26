# import colander
# from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config

# from questy.arrival import create_arrival_and_or_page, arrival_pages
# from questy.resources import PageJSONListAdapter
# from questy.schema import ArriveSchema


@view_config(
    route_name='arrivals',
    renderer='json',
    request_method='POST',
    permission='arrive',
)
def arrive(request):
    return {
        'message': "first arrival",
        'is_first': True,
        'page': {
            'url': '/api/pages/1',
        }
    }
#     schema = ArriveSchema()
#     try:
#         deserialized = schema.deserialize(request.POST)
#     except colander.Invalid as e:
#         return HTTPBadRequest(e)
#
#     url = deserialized['url']
#     arrival, created = create_arrival_and_or_page(request.user, url)
#     if created:
#         msg = 'First arrival'
#     else:
#         msg = 'Arrived'
#     return {
#         'message':  msg,
#         'page': arrival.page,
#     }


@view_config(
    route_name='arrivals',
    renderer='json',
    request_method='GET',
    permission='view',
)
def list_arrivals(request):
    return {
        'message': "OK",
        'pages': [
            {'url': '/api/pages/1'},
        ]
    }
#     user_id = request.GET.get('user_id')
#     return {
#         'message': 'OK',
#         'pages': [PageJSONListAdapter(request, page)
#                   for page in arrival_pages(user_id)]
#     }
