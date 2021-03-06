import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_translogger',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'colander',
    'redis',
]

setup(name='questy',
      version='0.0',
      description='questy',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='questy',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = questy:main
      [console_scripts]
      initialize_questy_db = questy.scripts.initializedb:main
      create_questy_user = questy.scripts.createuser:main
      makelots = questy.scripts.makelots:main
      """)
