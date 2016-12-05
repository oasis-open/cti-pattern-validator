from distutils.core import setup

setup(
    name='cybox-pattern-validator',
    version='0.2.0',
    packages=['pattern_validator', 'pattern_validator.grammars'],
    description='Validate CybOX patterns',
    install_requires=[
        "antlr4-python2-runtime==4.5.3 ; python_version < '3'",
        "antlr4-python3-runtime==4.5.3 ; python_version >= '3'",
        "enum34 ; python_version < '3.4'",
        "six",
    ]
)
