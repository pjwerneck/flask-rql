# -*- coding: utf-8 -*-

import os
import re
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'test':
    try:
        __import__('pytest')
    except ImportError:
        print('pytest required.')
        sys.exit(1)

    errors = os.system('pytest')
    sys.exit(bool(errors))


with open('rqlalchemy/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()


install = [
    'pyrql',
    'sqlalchemy',
]


packages = [
    'rqlalchemy',
]

setup(
    name='rqlalchemy',
    version=version,
    description='Resource Query Language for SQLAlchemy',
    long_description=long_description,
    packages=packages,
    tests_require=['pytest'],
    install_requires=install,
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
