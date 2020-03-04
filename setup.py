#!/usr/bin/env python

from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

doc_requires = [
    'sphinx',
    'sphinx-prompt',
]

test_requires = [
    'coverage',
    'pytest',
    'pytest-cov',
]

dev_requires = doc_requires + test_requires + [
    'bumpversion',
    'check-manifest',
    'pre-commit',
    # test_requires are installed into every tox environment, so we don't
    # want to include tox there.
    'tox',
]

setup(
    name='stix2-patterns',
    version='1.3.0',
    description='Validate STIX 2 Patterns.',
    long_description=readme,
    long_description_content_type='text/x-rst',
    url="https://github.com/oasis-open/cti-pattern-validator",
    author='OASIS Cyber Threat Intelligence Technical Committee',
    author_email='cti-users@lists.oasis-open.org',
    maintainer='Chris Lenk',
    maintainer_email='clenk@mitre.org',
    packages=find_packages(),
    install_requires=[
        'antlr4-python2-runtime~=4.8.0 ; python_version<"3"',
        'antlr4-python3-runtime~=4.8.0 ; python_version>="3"',
        'six',
        'typing ; python_version<"3.5" and python_version>="3"',
        'enum34 ; python_version<"3.4"',
    ],
    package_data={
        'stix2patterns.test.v20': ['spec_examples.txt'],
        'stix2patterns.test.v21': ['spec_examples.txt'],
    },
    entry_points={
        'console_scripts': [
            'validate-patterns = stix2patterns.validator:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    extras_require={
        'dev': dev_requires,
        'docs': doc_requires,
        'test': test_requires,
    },
)
