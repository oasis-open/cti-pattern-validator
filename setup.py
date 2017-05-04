#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='stix2-patterns',
    version='0.3.0',
    packages=find_packages(),
    description='Validate STIX 2 Patterns.',
    long_description=readme,
    install_requires=[
        "six",
        'antlr4-python2-runtime==4.7 ; python_version<"3"',
        'antlr4-python3-runtime==4.7 ; python_version>="3"',
        'typing ; python_version<"3.5" and python_version>="3"',
        'enum34 ; python_version~="3.3.0"'
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
