USERS = {'user': 'user',
         'viewer': 'viewer',
         'hirokiky@gmail.com': 'test'}
GROUPS = {'user': ['group:loginedusers'],
          'hirokiky@gmail.com': ['group:loginedusers']}


def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
