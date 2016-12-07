# cti-pattern-validator

*This is an [OASIS Open Repository](https://www.oasis-open.org/resources/open-repositories/). See the [Governance](#governance) section for more information.*

The STIX 2 Pattern Validator is a software tool for checking the syntax of the Cyber Threat Intelligence (CTI) STIX Pattern expressions, which are used within STIX to express conditions (represented with the Cyber Observable data model) that indicate particular cyber threat activity. The repository contains source code, an ANTLR grammar, automated tests and associated documentation for the tool. The validator can be used as a command-line tool or as a Python library which can be included in other applications.

[![Travis-CI Build Status](https://api.travis-ci.org/oasis-open/cti-pattern-validator.svg?branch=master)](https://travis-ci.org/oasis-open/cti-pattern-validator)

## Requirements

- [Python](https://www.python.org) 2.7, 3.3, 3.4, or 3.5
- ANTLR grammar runtime (4.5.3 or newer):
    - [antlr4-python2-runtime](https://pypi.python.org/pypi/antlr4-python2-runtime) (Python 2.7)
    - [antlr4-python3-runtime](https://pypi.python.org/pypi/antlr4-python3-runtime) (Python 3)
- [enum34](https://pypi.python.org/pypi/enum34) (Python 3.3)
- [six](https://pypi.python.org/pypi/six)

## Installation

Using [pip](https://pip.pypa.io) is highly recommended:

```bash
$ pip install stix2-patterns
```

For more information about installing Python packages, see the [Python
Packaging User Guide](https://packaging.python.org/installing/).

## Usage

The STIX Pattern Validator provides an executable script (`validate-patterns`)
in addition to being an importable Python library.

The `validate-patterns` script accepts patterns from either direct user input
or a file passed as an option.

### User Input

When prompted, enter a pattern to validate and press enter. The validator will
supply whether the pattern has passed or failed. If the pattern fails the test,
the validator will supply where the first syntax error occurred. The validator
will continue to prompt for patterns until Ctrl-C is pressed. Example:

```bash
$ validate-patterns

Enter a pattern to validate: [file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4']

PASS: [file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4']
```

### File Input

```bash
$ validate-patterns -f <path_to_file>
```

Use \<path\_to\_file> to specify the path to a file containing a set of
patterns to validate. Each pattern must be on a separate line of the file so
that the validator may determine where the pattern begins and ends. The
validator will supply the PASS/FAIL result of each pattern.

## Testing

The STIX Pattern Validator's test suite can be run with
[pytest](http://pytest.org).

You can also test against the examples provided in the supplied `examples.txt`
file.

```bash
$ validate-patterns -f stix2patterns/examples.txt
```

## Updating the Grammar

If you modify STIXGrammar.g4, you'll need to use the Java ANTLR package to generate new Python source files (the ANTLR .jar file is not needed for normal use of the validator).

1. Download antlr-4.5.3-complete.jar from http://www.antlr.org/download/
2. From the `grammars` directory, run

    ```bash
    $ java -cp "/path/to/antlr-4.5.3-complete.jar" -Xmx500M org.antlr.v4.Tool -Dlanguage=Python2 STIXPattern.g4
    ```

## Governance

This GitHub public repository ( **[https://github.com/oasis-open/cti-pattern-validator](https://github.com/oasis-open/cti-pattern-validator)** ) was [proposed](https://lists.oasis-open.org/archives/cti/201609/msg00001.html) and [approved](https://www.oasis-open.org/committees/ballot.php?id=2971) [[bis](https://issues.oasis-open.org/browse/TCADMIN-2431)] by the [OASIS Cyber Threat Intelligence (CTI) TC](https://www.oasis-open.org/committees/cti/) as an [OASIS Open Repository](https://www.oasis-open.org/resources/open-repositories/) to support development of open source resources related to Technical Committee work.

While this Open Repository remains associated with the sponsor TC, its development priorities, leadership, intellectual property terms, participation rules, and other matters of governance are [separate and distinct](https://github.com/oasis-open/cti-pattern-validator/blob/master/CONTRIBUTING.md#governance-distinct-from-oasis-tc-process) from the OASIS TC Process and related policies.

All contributions made to this Open Repository are subject to open source license terms expressed in the [BSD-3-Clause License](https://www.oasis-open.org/sites/www.oasis-open.org/files/BSD-3-Clause.txt). That license was selected as the declared ["Applicable License"](https://www.oasis-open.org/resources/open-repositories/licenses) when the Open Repository was created.

As documented in ["Public Participation Invited](https://github.com/oasis-open/cti-pattern-validator/blob/master/CONTRIBUTING.md#public-participation-invited)", contributions to this OASIS Open Repository are invited from all parties, whether affiliated with OASIS or not. Participants must have a GitHub account, but no fees or OASIS membership obligations are required. Participation is expected to be consistent with the [OASIS Open Repository Guidelines and Procedures](https://www.oasis-open.org/policies-guidelines/open-repositories), the open source [LICENSE](https://github.com/oasis-open/cti-pattern-validator/blob/master/LICENSE) designated for this particular repository, and the requirement for an [Individual Contributor License Agreement](https://www.oasis-open.org/resources/open-repositories/cla/individual-cla) that governs intellectual property.

### <a id="maintainers">Maintainers</a>

Open Repository [Maintainers](https://www.oasis-open.org/resources/open-repositories/maintainers-guide) are responsible for oversight of this project's community development activities, including evaluation of GitHub [pull requests](https://github.com/oasis-open/cti-pattern-validator/blob/master/CONTRIBUTING.md#fork-and-pull-collaboration-model) and [preserving](https://www.oasis-open.org/policies-guidelines/open-repositories#repositoryManagement) open source principles of openness and fairness. Maintainers are recognized and trusted experts who serve to implement community goals and consensus design preferences.

Initially, the associated TC members have designated one or more persons to serve as Maintainer(s); subsequently, participating community members may select additional or substitute Maintainers, per [consensus agreements](https://www.oasis-open.org/resources/open-repositories/maintainers-guide#additionalMaintainers).

#### <a id="currentMaintainers">Current Maintainers of this Open Repository</a>

 * [Greg Back](mailto:gback@mitre.org); GitHub ID: [https://github.com/gtback](https://github.com/gtback); WWW: [MITRE](https://www.mitre.org)
 * [Ivan Kirillov](mailto:ikirillov@mitre.org); GitHub ID: [https://github.com/ikiril01](https://github.com/ikiril01); WWW: [MITRE](https://www.mitre.org)

## <a id="aboutOpenRepos">About OASIS Open Repositories</a>

 * [Open Repositories: Overview and Resources](https://www.oasis-open.org/resources/open-repositories/)
 * [Frequently Asked Questions](https://www.oasis-open.org/resources/open-repositories/faq)
 * [Open Source Licenses](https://www.oasis-open.org/resources/open-repositories/licenses)
 * [Contributor License Agreements (CLAs)](https://www.oasis-open.org/resources/open-repositories/cla)
 * [Maintainers' Guidelines and Agreement](https://www.oasis-open.org/resources/open-repositories/maintainers-guide)

## <a id="feedback">Feedback</a>

Questions or comments about this Open Repository's activities should be composed as GitHub issues or comments. If use of an issue/comment is not possible or appropriate, questions may be directed by email to the Maintainer(s) [listed above](#currentMaintainers). Please send general questions about Open Repository participation to OASIS Staff at [repository-admin@oasis-open.org](mailto:repository-admin@oasis-open.org) and any specific CLA-related questions to [repository-cla@oasis-open.org](mailto:repository-cla@oasis-open.org).
