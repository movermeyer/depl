#!/usr/bin/env python

from __future__ import with_statement
try:
    from setuptools import setup
except ImportError:
    # Distribute is not actually required to install
    from distutils.core import setup

__AUTHOR__ = 'David Halter'
__AUTHOR_EMAIL__ = 'davidhalter88@gmail.com'

readme = open('README.rst').read() + '\n\n' + open('CHANGELOG.rst').read()

import depl
VERSION = '.'.join(str(x) for x in depl.__version__)

setup(name='depl',
      version=VERSION,
      description='depl - deploy easy and fast.',
      author=__AUTHOR__,
      author_email=__AUTHOR_EMAIL__,
      maintainer=__AUTHOR__,
      maintainer_email=__AUTHOR_EMAIL__,
      url='https://github.com/davidhalter/depl',
      license='MIT',
      keywords='python deployment fabric',
      long_description=readme,
      packages=['depl'],
      platforms=['any'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: User Interfaces',
          'Topic :: System :: Software Distribution',
      ],
    )