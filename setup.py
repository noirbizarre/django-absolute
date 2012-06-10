#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-absolute',
    version=__import__('absolute').__version__,
    description=__import__('absolute').__description__,
    long_description=open('README.rst').read(),
    url='https://github.com/noirbizarre/django-absolute',
    author='Axel Haustant',
    author_email='noirbizarre+absolute@gmail.com',
    maintainer='Axel Haustant',
    maintainer_email='noirbizarre+absolute@gmail.com',
    packages=['absolute', 'absolute.templatetags'],
    install_requires=['django'],
)
