# --------------------------------------------
# Copyright 2020, Grant Viklund
# @Author: Grant Viklund
# @Date:   2020-08-18 10:50:10
# --------------------------------------------

from os import path
from setuptools import setup, find_packages

file_path = path.abspath(path.dirname(__file__))

with open(path.join(file_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

package_metadata = {
    'name': 'django-saasy',
    'version': '0.1.0',
    'description': "Common features used in SaaS applications",
    'long_description': long_description,
    'url': 'https://github.com/renderbox/django-saasy/',
    'author': 'Grant Viklund',
    'author_email': 'renderbox@gmail.com',
    'license': 'Not open source',
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    'keywords': ['django', 'app'],
}

setup(
    **package_metadata,
    packages=find_packages(),
    package_data={'saasy': ['*.html']},
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        'Django>=3.0,<3.1',
        'djangorestframework',
        'dj-database-url',
    ],
    extras_require={
        'dev': [
            'django-crispy-forms',
            'django-allauth',
        ],
        'test': [],
        'prod': [],
        'build': [
            'setuptools',
            'wheel',
            'twine',
        ],
        'docs': [
            'coverage',
            'Sphinx',
            'sphinx-bootstrap-theme',
            'sphinx-rtd-theme',
            'sphinx-autobuild',
        ],
    }
)