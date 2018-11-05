Usage
=====

The STIX Pattern Validator provides an executable script (``validate-patterns``)
in addition to being an importable Python library.

The ``validate-patterns`` script accepts patterns from either direct user input
or a file passed as an option.

From Python Code
----------------

The ``run_validator`` function can be called on any Python string. It returns a
list of errors encountered while parsing the pattern.

.. code:: python

    from stix2patterns.validator import run_validator

    pattern = "[file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4']"
    errors = run_validator(pattern)

User Input
----------

When prompted, enter a pattern to validate and press enter. The validator will
supply whether the pattern has passed or failed. If the pattern fails the test,
the validator will supply where the first syntax error occurred. The validator
will continue to prompt for patterns until Ctrl-C is pressed. Example:

.. code:: bash

    $ validate-patterns

    Enter a pattern to validate: [file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4']

    PASS: [file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4']

File Input
----------

.. code:: bash

    $ validate-patterns -f <path_to_file>

Use <path\_to\_file> to specify the path to a file containing a set of patterns
to validate. Each pattern must be on a separate line of the file so that the
validator may determine where the pattern begins and ends. The validator will
supply the PASS/FAIL result of each pattern.