#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pytest-runner',
    # TODO: put package requirements here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='cashflow',
    version='0.1.0',
    description="Django powered budgeting webapp for tracking personal finances",
    long_description=readme + '\n\n' + history,
    author="Jules Houts",
    author_email='jhouts@gmail.com',
    url='https://github.com/jchouts/cashflow',
    packages=[
        'cashflow',
    ],
    package_dir={'cashflow':
                 'cashflow'},
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=False,
    keywords='cashflow',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
