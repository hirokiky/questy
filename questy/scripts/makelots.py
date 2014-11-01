import os
import sys
import transaction

from pyramid.paster import bootstrap

from questy.models import (
    DBSession,
    User,
    Comment,
    Page
)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    bootstrap(config_uri)

    with transaction.manager:
        comment = Comment()
        follower = User()
        following = User()

        page = Page()
        page.comments = [comment]
        follower.followings = [following]
        following.comments = [comment]

        DBSession.add(comment)
        DBSession.add(following)
        DBSession.add(follower)
        DBSession.add(page)
