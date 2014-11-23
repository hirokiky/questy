from datetime import datetime

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from questy.models import (
    DBSession,
    Base,
)
from pyramid.renderers import JSON

from questy.security import groupfinder, get_user
from questy import redisio
from questy import renderers


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    redisio.set_redis_client(settings['redis.client'],
                             host=settings['redis.host'],
                             port=settings['redis.port'],
                             db=settings['redis.db'])

    authn_policy = AuthTktAuthenticationPolicy(
        'sosecret', callback=groupfinder, hashalg='sha512'
    )
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings,
                          root_factory='questy.models.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    config.add_request_method(get_user, 'user', reify=True)

    json_renderer = JSON()
    json_renderer.add_adapter(datetime, renderers.datetime_adapter)
    config.add_renderer('json', json_renderer)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('top', '/')
    config.add_route('login', '/login/')
    config.add_route('logout', '/logout/')

    # api
    config.add_route('achievements', '/api/achievements')
    config.add_route('achievement', '/api/achievements/{achievement_id:\d+}')
    config.add_route('activities', '/api/activities')
    config.add_route('arrivals', '/api/arrivals')
    config.add_route('comments', 'api/comments')
    config.add_route('comment', '/api/comments/{comment_id:\d+}')
    config.add_route('upvote', '/api/comments/{comment_id:\d+}/upvote')
    config.add_route('downvote', '/api/comments/{comment_id:\d+}/downvote')
    config.add_route('page', '/api/pages/{page_id:\d+}')
    config.add_route('user', '/api/users/{user_id:\d+}')
    config.add_route('follow', '/api/users/{user_id:\d+}/follow')
    config.add_route('unfollow', '/api/users/{user_id:\d+}/unfollow')
    config.add_route('followers', '/api/users/{user_id:\d+}/follower')
    config.add_route('followings', '/api/users/{user_id:\d+}/following')
    config.scan()
    return config.make_wsgi_app()
