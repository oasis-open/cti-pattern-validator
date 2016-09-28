<div>
<h1>README</h1>

<div>
<h2><a id="readme-general">OASIS Open Repository: cti-pattern-validator</a></h2>

<p>This GitHub public repository ( <b><a href="https://github.com/oasis-open/cti-pattern-validator">https://github.com/oasis-open/cti-pattern-validator</a></b> ) was created at the request of the <a href="https://www.oasis-open.org/committees/cti/">OASIS Cyber Threat Intelligence (CTI) TC</a> as an <a href="https://www.oasis-open.org/resources/open-repositories/">OASIS Open Repository</a> to support development of open source resources related to Technical Committee work.</p>

<p>While this Open Repository remains associated with the sponsor TC, its development priorities, leadership, intellectual property terms, participation rules, and other matters of governance are <a href="https://github.com/oasis-open/cti-pattern-validator/blob/master/CONTRIBUTING.md#governance-distinct-from-oasis-tc-process">separate and distinct</a> from the OASIS TC Process and related policies.</p>

<p>All contributions made to this Open Repository are subject to open source license terms expressed in the <a href="https://www.oasis-open.org/sites/www.oasis-open.org/files/BSD-3-Clause.txt">BSD-3-Clause License</a>.  That license was selected as the declared <a href="https://www.oasis-open.org/resources/open-repositories/licenses">"Applicable License"</a> when the Open Repository was created.</p>

<p>As documented in <a href="https://github.com/oasis-open/cti-pattern-validator/blob/master/CONTRIBUTING.md#public-participation-invited">"Public Participation Invited</a>", contributions to this OASIS Open Repository are invited from all parties, whether affiliated with OASIS or not.  Participants must have a GitHub account, but no fees or OASIS membership obligations are required.  Participation is expected to be consistent with the <a href="https://www.oasis-open.org/policies-guidelines/open-repositories">OASIS Open Repository Guidelines and Procedures</a>, the open source <a href="https://github.com/oasis-open/cti-pattern-validator/blob/master/LICENSE">LICENSE</a> designated for this particular repository, and the requirement for an <a href="https://www.oasis-open.org/resources/open-repositories/cla/individual-cla">Individual Contributor License Agreement</a> that governs intellectual property.</p>

</div>

<div>
<h2><a id="purposeStatement">Statement of Purpose</a></h2>

<p>Statement of Purpose for this OASIS Open Repository (cti-pattern-validator) as <a href="https://lists.oasis-open.org/archives/cti/201609/msg00001.html">proposed</a> and <a href="https://www.oasis-open.org/committees/ballot.php?id=2971">approved</a> [<a href="https://issues.oasis-open.org/browse/TCADMIN-2431">bis</a>] by the TC:</p>

<p>The pattern-validator is a software tool for checking the syntax of the Cyber Threat Intelligence (CTI) STIX/CybOX Patterning expressions, which are used within STIX to express conditions (represented with the CybOX data model) that indicate particular cyber threat activity. The repository contains source code, an ANTLR grammar, automated tests and associated documentation for the tool. The pattern-validator can be used as a command-line tool or as a Python library which can be included in other applications.</p>


</div>

## Requirements

-   Python 2.7.6+ or Python 3.4.0+
-   For Python 2: antlr4-python2-runtime 4.5.3+
    (<https://pypi.python.org/pypi/antlr4-python2-runtime>)
-   For Python 3: antlr4-python3-runtime 4.5.3+
    (<https://pypi.python.org/pypi/antlr4-python3-runtime>)
-   To run test script - pytest
    (<http://pytest.org/latest/getting-started.html>)

## Installation

1.  Install the antlr4 python runtime module from the above link using
    the `MS Windows Installer` option for Windows **OR** download and
    unzip the source code and run:

    ```bash
    $ python setup.py install
    ```

2.  Download zip file or source code for pattern-validator. Unzip the
    source code if necessary and once again run:

    ```bash
    $ python setup.py install
    ```

## Usage

There are two ways to enter patterns into this tool using the command
line:

- via direct user input
- by taking a specified file of patterns

### User Input

Navigate to the pattern\_validator folder and type the following on the
command line:

```bash
$ python pattern_validator.py
```

When prompted, enter a pattern to validate and press enter. The
validator will supply whether the pattern has passed or failed. If the
pattern fails the test, the validator will supply where the first syntax
error occurred. The validator will continue to prompt for patterns until
Ctrl-C is pressed. Example:

```bash
$ python pattern_validator.py

Enter a pattern to validate:
file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4'

PASS: file-object:hashes.md5 = '79054025255fb1a26e4bc422aef54eb4'
```

### File

Navigate to the pattern\_validator folder and type the following on the
command line:

```bash
$ python pattern_validator.py -f <path_to_file>
```

Use &lt;path\_to\_file&gt; to specify the path to a file containing a
set of patterns to validate. Each pattern must be on a separate line of
the file so that the validator may determine where the pattern begins
and ends. The validator will supply the PASS/FAIL result of each
pattern.

## Testing

The file `test_pattern_validator.py` in the **test** directory is
supplied in order to test your installation of the pattern validator. To
run this test script, **pytest** must be installed on your system. This
script should output the validation results of the patterns found within
the `test_pattern_validator.py` script. To execute the tests, simply run
the following within the same directory as this script:

```bash
$ py.test
```

If **pytest** is not installed on your system, you can test your
installation by running the following command:

```bash
$ python pattern_validator.py -f test/pattern_validator_test_cases.txt
```


<div>
<h2><a id="maintainers">Maintainers</a></h2>

<p>Open Repository <a href="https://www.oasis-open.org/resources/open-repositories/maintainers-guide">Maintainers</a> are responsible for oversight of this project's community development activities, including evaluation of GitHub <a href="https://github.com/oasis-open/cti-pattern-validator/blob/master/CONTRIBUTING.md#fork-and-pull-collaboration-model">pull requests</a> and <a href="https://www.oasis-open.org/policies-guidelines/open-repositories#repositoryManagement">preserving</a> open source principles of openness and fairness. Maintainers are recognized and trusted experts who serve to implement community goals and consensus design preferences.</p>

<p>Initially, the associated TC members have designated one or more persons to serve as Maintainer(s); subsequently, participating community members may select additional or substitute Maintainers, per <a href="https://www.oasis-open.org/resources/open-repositories/maintainers-guide#additionalMaintainers">consensus agreements</a>.</p>

<p><b><a id="currentMaintainers">Current Maintainers of this Open Repository</a></b></p>

<ul>

<!--  Initial Maintainers: Greg Back & Ivan Kirillov  -->

<li><a href="mailto:gback@mitre.org">Greg Back</a>; GitHub ID: <a href="https://github.com/gtback">https://github.com/gtback</a>;  WWW: <a href="https://www.mitre.org">MITRE</a></li>

<li><a href="mailto:ikirillov@mitre.org">Ivan Kirillov</a>; GitHub ID: <a href="https://github.com/ikiril01">https://github.com/ikiril01</a>;  WWW: <a href="https://www.mitre.org">MITRE</a></li>

<!-- 
<li><a href="mailto:trey@kingfisherops.com">Trey Darley</a>; GitHub ID: <a href="https://github.com/treyka/">https://github.com/treyka/</a>; WWW: <a href="http://kingfisherops.com/">Kingfisher Operations</a></li> -->

</ul>

</div>

<div><h2><a id="aboutOpenRepos">About OASIS Open Repositories</a></h2>

<p><ul>
<li><a href="https://www.oasis-open.org/resources/open-repositories/">Open Repositories: Overview and Resources</a></li>
<li><a href="https://www.oasis-open.org/resources/open-repositories/faq">Frequently Asked Questions</a></li>
<li><a href="https://www.oasis-open.org/resources/open-repositories/licenses">Open Source Licenses</a></li>
<li><a href="https://www.oasis-open.org/resources/open-repositories/cla">Contributor License Agreements (CLAs)</a></li>
<li><a href="https://www.oasis-open.org/resources/open-repositories/maintainers-guide">Maintainers' Guidelines and Agreement</a></li>
</ul></p>

</div>

<div><h2><a id="feedback">Feedback</a></h2>

<p>Questions or comments about this Open Repository's activities should be composed as GitHub issues or comments. If use of an issue/comment is not possible or appropriate, questions may be directed by email to the Maintainer(s) <a href="#currentMaintainers">listed above</a>.  Please send general questions about Open Repository participation to OASIS Staff at <a href="mailto:repository-admin@oasis-open.org">repository-admin@oasis-open.org</a> and any specific CLA-related questions to <a href="mailto:repository-cla@oasis-open.org">repository-cla@oasis-open.org</a>.</p>

</div></div>
