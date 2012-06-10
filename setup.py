#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='django-absolute',
    version=__import__('absolute').__version__,
    description=__import__('absolute').__description__,
    long_description=open('README.rst').read(),
    url='https://github.com/noirbizarre/django-absolute',
    download_url='http://pypi.python.org/pypi/django-absolute',
    author='Axel Haustant',
    author_email='noirbizarre+absolute@gmail.com',
    packages=['absolute', 'absolute.templatetags'],
    install_requires=['django'],
    license='LGPL',
    classifiers=[
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: System :: Software Distribution",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
)
