#!/usr/bin/env python

from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()


def get_version():
    with open('stix2patterns/version.py') as f:
        for line in f.readlines():
            if line.startswith("__version__"):
                version = line.split()[-1].strip('"')
                return version
        raise AttributeError("Package does not have a __version__")


doc_requires = [
    'sphinx',
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
    'readme_renderer',
    # test_requires are installed into every tox environemnt, so we don't
    # want to include tox there.
    'tox',
]

setup(
    name='stix2-patterns',
    version=get_version(),
    description='Validate STIX 2 Patterns.',
    long_description=readme,
    url="https://github.com/oasis-open/cti-pattern-validator",
    author='OASIS Cyber Threat Intelligence Technical Committee',
    author_email='cti-users@lists.oasis-open.org',
    maintainer='Greg Back',
    maintainer_email='gback@mitre.org',
    packages=find_packages(),
    install_requires=[
        'antlr4-python2-runtime>=4.7 ; python_version<"3"',
        'antlr4-python3-runtime>=4.7 ; python_version>="3"',
        'six',
        'typing ; python_version<"3.5" and python_version>="3"',
    ],
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
    ],
    extras_require={
        'dev': dev_requires,
        'docs': doc_requires,
        'test': test_requires,
    },
)
