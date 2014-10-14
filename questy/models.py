from sqlalchemy import (
    Column,
    ForeignKey,
    Table,

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


follow = Table(
    'follow',
    Base.metadata,

    Column('follower_id', Integer, ForeignKey('adventurer.adventurer_id')),
    Column('following_id', Integer, ForeignKey('adventurer.adventurer_id')),
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


class Adventurer(Base):
    __tablename__ = 'adventurer'
    adventurer_id = Column(Integer, primary_key=True)
    name = Column(String(15), index=True, unique=True)
    email = Column(String(255), index=True, unique=True)
    password = Column(String(32))
    style = Column(Enum('C', 'H', name='style_types'))
    icon_path = Column(String(255))
    bio = Column(Text)
    url = Column(String(255))
    location = Column(String(3))  # ISO3166
    language = Column(String(3))  # ISO639
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    followings = relationship(
        'Adventurer',
        secondary=follow,
        primaryjoin=(follow.c.follower_id == adventurer_id),
        secondaryjoin=(follow.c.following_id == adventurer_id),
        backref='followers',
    )


class Achievement(Base):
    __tablename__ = 'achievement'
    achievement_id = Column(Integer, primary_key=True)
    reward_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


class EarnedAchievement(Base):
    __tablename__ = 'earned_achievement'
    earned_achievement_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


class Page(Base):
    __tablename__ = 'page'
    page_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


class Arrival(Base):
    __tablename__ = 'arrival'
    arrival_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


class Upvote(Base):
    __tablename__ = 'upvote'
    upvote_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())


class Downvote(Base):
    __tablename__ = 'downvote'
    downvote_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())
