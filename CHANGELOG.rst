CHANGELOG
=========

1.0.0 - Released 2018-07-18
---------------------------

* #34 - Add documentation on ReadTheDocs: https://stix2-patterns.readthedocs.io/
* #39 - Raise error for unexepected unused character values.
* #41 - Raise error for negative REPEAT values.
* #42 - Improved Timestamp validation.
* #43 - Validate Base64 binary literals.
* #48 - Make pattern qualifier and operator keywords case-sensitive.
* Drop support for Python 2.6 and 3.3.

0.6.0 - Released 2017-11-13
---------------------------

* #32 - Added a public walk() method to the Pattern class. (@chisholm)
* Make repository structure match other projects. (@emmanvg)

0.5.0 - Released 2017-07-12
---------------------------

* Separate object and path components in inspector.
* Support "NOT" qualifier on all comparison operators.

0.4.1 - Released 2017-05-19
---------------------------

* Repackaged to not use a Wheel distribution

0.4.0 - Released 2017-05-19
---------------------------

* Encapsulated parsed patterns in a new Pattern class

0.3.0 - Released 2017-05-04
---------------------------

* Update for STIX 2.0 WD02.
* Add "inspector" module to extract features from patterns.
* Improve error messages.
* Update to ANTLR 4.7
* Add testing for Python 2.6 and 3.6

0.2.2 - Released 2017-03-01
---------------------------

* Update packaging to install correct ANTLR4 runtime depending on Python
  version.

0.2.0 - Released 2017-02-24
---------------------------

* Initial public version.
