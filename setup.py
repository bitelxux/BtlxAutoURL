from setuptools import setup

PACKAGE = 'BtlxAutoURL'
VERSION = '0.1'

setup(name=PACKAGE,
      version=VERSION,
      packages=['btlxautourl'],
      entry_points={'trac.plugins': '%s = btlxautourl' % PACKAGE},
      author="Bitelxux",
      maintainer="Bitelxux",
      maintainer_email="bitelxux@gmail.com",
      description="""Autoexpand urls from plain text based 
                     on trac.ini btlxautourl section
                  """,
      license="GNU",
      url="",

)
