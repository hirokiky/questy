class PageJSONListAdapter(object):
    def __init__(self, request, page):
        self.request = request
        self.page = page

    def __json__(self, request):
        return {'page_id': self.page.page_id,
                'created_at': self.page.created_at}


class PageJSONDetailAdapter(object):
    def __init__(self, request, page):
        self.request = request
        self.page = page

    def __json__(self, request):
        return {'page_id': self.page.page_id,
                'page_url': self.page.page_url,
                'title': self.page.title,
                'summary_image_url': self.page.summary_image_url,
                'description': self.page.description,
                'created_at': self.page.created_at}
