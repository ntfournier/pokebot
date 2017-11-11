#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

# Package meta-data.
NAME = 'pokebot'
DESCRIPTION = 'A simple bot that play Pokemon using image recognition'
URL = 'https://github.com/ntfournier/pokebot'
EMAIL = 'vince@ntfournier.com'
AUTHOR = 'Vincent Fournier'

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    entry_points={
        "console_scripts": ['pokebot=pokebot.main:main']
    },
    test_suite='nose.collector',
    tests_require=['nose'],
    license='GPL-v3.0'
)