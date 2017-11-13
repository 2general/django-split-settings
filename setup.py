# -*- coding: utf-8 -*-

"""
Setup file for django-split-settings.

Visit https://pypi.python.org/pypi/django-split-settings
for more information.
"""

import io

from setuptools import setup

from split_settings import __version__

INSTALL_REQUIRES = []  # no deps

TESTS_REQUIRE = [
    'six',

    # pytest plugins:
    'pytest-cov',
    'pytest-isort',

    # Linting:
    'flake8-builtins',
    'flake8-commas',
    'flake8-quotes',
    'flake8<3.6.0',  # fixes dependency resolution
    'pytest-flake8',

    # This line should be the last one:
    # https://github.com/pytest-dev/pytest-runner/issues/11
    'pytest==3.0.7',  # should be the last
]

SETUP_REQUIRES = [
    'pytest-runner',
]

with io.open('README.rst', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='django-split-settings',
    version=__version__,
    description=(
        'Organize Django settings into multiple files and directories. '
        'Easily override and modify settings. Use wildcards and optional '
        'settings files.'
    ),
    long_description=LONG_DESCRIPTION,
    author='Nikita Sobolev, Visa Kopu, Antti Kaihola',
    author_email='mail@sobolevn.me',
    url='http://github.com/sobolevn/django-split-settings',
    packages=[
        'split_settings',
    ],
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    setup_requires=SETUP_REQUIRES,
    zip_safe=False,
    keywords=[
        'django',
        'settings',
        'configuration',
        'config',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.5',
        'Framework :: Django :: 1.6',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
