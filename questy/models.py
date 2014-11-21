from pyramid.security import Allow, Everyone
from sqlalchemy import (
    Column,
    ForeignKey,
    Table,

    Boolean,
    DateTime,
    Enum,
    Integer,
    String,
    Text,
)
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    relationship,
    scoped_session,
    sessionmaker,
)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),
               (Allow, 'group:general', 'edit')]

    def __init__(self, request):
        pass


earned_achievement = Table(
    'earned_achievement',
    Base.metadata,

    Column('user_id', Integer, ForeignKey('user.user_id')),
    Column('achievement_id', Integer, ForeignKey('achievement.achievement_id')),
    Column('created_at', DateTime, server_default=func.now()),
    Column('updated_at', DateTime, server_onupdate=func.now()),
)


class Achievement(Base):
    __tablename__ = 'achievement'
    achievement_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    image_path = Column(String(255))
    point = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


follow = Table(
    'follow',
    Base.metadata,

    Column('follower_id', Integer, ForeignKey('user.user_id')),
    Column('following_id', Integer, ForeignKey('user.user_id')),
    Column('created_at', DateTime, server_default=func.now()),
    Column('updated_at', DateTime, server_onupdate=func.now()),
)


STYLE_DISPLAY_MAPPING = {
    'casual': 'Casual',
    'hardcore': 'Hardcore',
}

STYLE_CODE_MAPPING = {
    'casual': 'C',
    'hardcore': 'H',
}


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(15), index=True, unique=True)
    email = Column(String(255), index=True, unique=True)
    password = Column(String(32))
    admin = Column(Boolean, default=False)
    style = Column(Enum('C', 'H', name='style_types'))
    icon_path = Column(String(255))
    bio = Column(Text)
    url = Column(String(255))
    location = Column(String(3))  # ISO3166
    language = Column(String(3))  # ISO639
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    followings = relationship(
        'User',
        secondary=follow,
        primaryjoin=(follow.c.follower_id == user_id),
        secondaryjoin=(follow.c.following_id == user_id),
        backref='followers',
    )
    earned_achievements = relationship(
        'Achievement',
        secondary=earned_achievement,
    )
    arrivals = relationship('Arrival')
    comments = relationship('Comment')
    upvotes = relationship('Upvote')
    downvotes = relationship('Downvote')

    logged_in = True


class AnnonymousUser(object):
    logged_in = False


class Page(Base):
    __tablename__ = 'page'
    page_id = Column(Integer, primary_key=True)
    url = Column(String(4095), index=True)
    title = Column(String(255))
    summary_image_url = Column(String(4095))
    description = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    arrivals = relationship('Arrival')
    comments = relationship('Comment')


class Arrival(Base):
    __tablename__ = 'arrival'
    arrival_id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey('page.page_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    page_id = Column(Integer, ForeignKey('page.page_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    body = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    upvotes = relationship('Upvote')
    downvotes = relationship('Downvote')


class Upvote(Base):
    __tablename__ = 'upvote'
    upvote_id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.comment_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


class Downvote(Base):
    __tablename__ = 'downvote'
    downvote_id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.comment_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())
