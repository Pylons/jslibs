##############################################################################
#
# Copyright (c) 2008-2011 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires = [
    'pyramid',
    ]

test_requires = [
    'nose',
    'coverage',
    ]



setup(name='jslibs',
      version='0.9',
      description=('A package which does stuff with js libs'),
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: JavaScript",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: Repoze Public License",
        ],
      keywords='wsgi pylons pyramid',
      author="Pylons Project Contributors",
      author_email="pylons-devel@googlegroups.com",
      url="http://docs.pylonsproject.org",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      #package_data={
      #  '': ['*.js', '*.css'],
      #  },
      zip_safe=False,
      install_requires=install_requires,
      tests_require=install_requires+test_requires,
      test_suite="jslibs",
      entry_points="""\
        [console_scripts]
            juice_jslibs = jslibs.juice_jslibs:main
            jslibs_prepare_sources = jslibs.jslibs_prepare_sources:main
        """,
      )
