#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='django-absolute',
    version=__import__('absolute').__version__,
    description=__import__('absolute').__description__,
    long_description=open('README.rst').read(),
    author='Axel Haustant',
    maintainer='Axel Haustant',
    maintainer_email='noirbizarre+absolute@gmail.com',
    packages=['absolute', 'absolute.templatetags'],
    install_requires=['django'],
)
