#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'flask', 'json-rpc']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Ghislain Picard",
    author_email='ghislain.picard@univ-grenoble-alpes.fr',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="make python function easily accessible from Node-RED ",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pynodered',
    name='pynodered',
    packages=find_packages(include=['pynodered', 'pynodered.imported_modules']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ghislainp/pynodered',
    version='0.1.0',
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'pynodered=pynodered.server:main',
        ],
    },
)
