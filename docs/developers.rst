Developer's Guide
=================

Updating the Grammar
--------------------

The ANTLR pattern grammar is maintained in the `stix2-json-schemas
<https://github.com/oasis-open/cti-stix2-json-schemas/blob/master/pattern_grammar/STIXPattern.g4>`__
repository. If the grammar changes, the code in this repository should be
updated to match. To do so, use the Java ANTLR package to generate new Python
source files. (The .jar file is not needed for normal use of the validator).

1. Download antlr-4.7.1-complete.jar from http://www.antlr.org/download/
2. Clone the stix2-json-schemas repository or download the STIXPattern.g4 file.
3. Change to the directory containing the STIXPattern.g4 file.
4. Run the following command

   .. code:: bash

       $ java -jar "/path/to/antlr-4.7.1-complete.jar" -Dlanguage=Python2 STIXPattern.g4 -visitor -o /path/to/cti-pattern-validator/stix2patterns/grammars

5. Commit the resulting files to git.

Testing
-------

The STIX Pattern Validator's test suite can be run with `pytest
<http://pytest.org>`__.

You can also test against the examples provided in the supplied example file.

.. code:: bash

    $ validate-patterns -f stix2patterns/test/spec_examples.txt
