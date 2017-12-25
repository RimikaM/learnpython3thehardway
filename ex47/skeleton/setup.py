# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:08:48 2017

@author: rimikamajumdar
"""

# setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Rimika Majumdar',
        'url': 'url to get the project at',
        'download_url': 'where to download project at',
        'author_email': 'my email',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
        }

setup(**config)