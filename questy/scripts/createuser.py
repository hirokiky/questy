import getpass
import os
import sys
import transaction

from pyramid.paster import bootstrap

from questy.models import (
    DBSession,
    User,
)
from questy.security import set_password


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

    email = input('Input Email:')
    password = getpass.getpass('Input Password:')

    user = User(email=email)
    set_password(user, password)

    with transaction.manager:
        DBSession.add(user)
