def setup_db():
    from sqlalchemy import create_engine
    from questy.models import DBSession, Base
    engine = create_engine('sqlite://')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)


def setup_redis():
    from questy import redisio
    redisio.set_redis_client('fakeredis.FakeStrictRedis')
