import hashlib
from sqlalchemy.orm.exc import NoResultFound

from pyramid.security import authenticated_userid

from questy.models import DBSession, User, AnnonymousUser


def make_hashed_password(password):
    encoded = password.encode()

    m = hashlib.sha1()
    m.update(encoded)
    return m.digest()


def set_password(user: User, password: str):
    user.password = make_hashed_password(password)
    return user


def validate_password(email, password):
    hashed_password = make_hashed_password(password)

    return DBSession.query(User).filter(
        (User.email == email) &
        (User.password == hashed_password)
    ).count() > 0


def groupfinder(email, request):
    try:
        user = DBSession.query(User).filter(User.email == email).one()
    except NoResultFound:
        return

    if user.admin:
        return ['group:general', 'group:admin']
    else:
        return ['group:general']


def get_user(request):
    email = authenticated_userid(request)
    try:
        user = DBSession.query(User).filter(User.email == email).one()
    except NoResultFound:
        return AnnonymousUser()

    return user
