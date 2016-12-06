#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='stix2-patterns',
    version='0.2.0',
    packages=find_packages(),
    description='Validate STIX 2 Patterns.',
    install_requires=[
        "antlr4-python2-runtime==4.5.3 ; python_version < '3'",
        "antlr4-python3-runtime==4.5.3 ; python_version >= '3'",
        "enum34 ; python_version < '3.4'",
        "six",
    ]
)
