#!/usr/bin/env python
from setuptools import setup
import os
import re

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def extract_version():
    init_file_content = read_file(os.path.join(BASE_DIR, 'binance', '__init__.py'))
    version_match = re.search(r'^__version__ = ["\']([^"\']+)', init_file_content, re.M)
    if not version_match:
        raise ValueError("Unable to find the version number.")
    return version_match.group(1)

setup(
    name='python-binance',
    version=extract_version(),
    packages=['binance'],
    description='Binance REST API python implementation',
    long_description=read_file("README.rst"),
    long_description_content_type="text/x-rst",
    url='https://github.com/sammchardy/python-binance',
    author='Sam McHardy',
    license='MIT',
    author_email='[email protected]',
    install_requires=[
        'requests', 'six', 'dateparser', 'aiohttp', 'ujson', 'websockets', 'pycryptodome'
    ],
    keywords='binance exchange rest api bitcoin ethereum btc eth neo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
