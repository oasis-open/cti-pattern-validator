"""
Validates a user entered pattern against STIXPattern grammar.
"""

from __future__ import print_function

import argparse

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
import six

from .grammars.STIXPatternLexer import STIXPatternLexer
from .grammars.STIXPatternParser import STIXPatternParser


class STIXPatternErrorListener(ErrorListener):
    """
    Modifies ErrorListener to collect error message and set flag to False when
    invalid pattern is encountered.
    """
    def __init__(self):
        super(STIXPatternErrorListener, self).__init__()
        self.err_strings = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.err_strings.append("FAIL: Error found at line %d:%d. %s" %
                                (line, column, msg))


def run_validator(pattern):
    """
    Validates a pattern against the STIX Pattern grammar.  Error messages are
    returned in a list.  The test passed if the returned list is empty.
    """

    start = ''
    if isinstance(pattern, six.string_types):
        start = pattern[:2]
        pattern = InputStream(pattern)

    if not start:
        start = pattern.readline()[:2]
        pattern.seek(0)

    parseErrListener = STIXPatternErrorListener()

    lexer = STIXPatternLexer(pattern)
    # it always adds a console listener by default... remove it.
    lexer.removeErrorListeners()

    stream = CommonTokenStream(lexer)

    parser = STIXPatternParser(stream)
    parser.buildParseTrees = False
    # it always adds a console listener by default... remove it.
    parser.removeErrorListeners()
    parser.addErrorListener(parseErrListener)

    # To improve error messages, replace "<INVALID>" in the literal
    # names with symbolic names.  This is a hack, but seemed like
    # the simplest workaround.
    for i, lit_name in enumerate(parser.literalNames):
        if lit_name == u"<INVALID>":
            parser.literalNames[i] = parser.symbolicNames[i]

    parser.pattern()

    # replace with easier-to-understand error message
    if not (start[0] == '[' or start == '(['):
        parseErrListener.err_strings[0] = "FAIL: Error found at line 1:0. " \
                                          "input is missing square brackets"

    return parseErrListener.err_strings


def validate(user_input, ret_errs=False, print_errs=False):
    """
    Wrapper for run_validator function that returns True if the user_input
    contains a valid STIX pattern or False otherwise. The error messages may
    also be returned or printed based upon the ret_errs and print_errs arg
    values.
    """

    errs = run_validator(user_input)
    passed = len(errs) == 0

    if print_errs:
        for err in errs:
            print(err)

    if ret_errs:
        return passed, errs

    return passed


def main():
    """
    Continues to validate patterns until it encounters EOF within a pattern
    file or Ctrl-C is pressed by the user.
    """
    parser = argparse.ArgumentParser(description='Validate STIX Patterns.')
    parser.add_argument('-f', '--file',
                        help="Specify this arg to read patterns from a file.",
                        type=argparse.FileType("r"))
    args = parser.parse_args()

    pass_count = fail_count = 0

    # I tried using a generator (where each iteration would run raw_input()),
    # but raw_input()'s behavior seems to change when called from within a
    # generator: I only get one line, then the generator completes!  I don't
    # know why behavior changes...
    import functools
    if args.file:
        nextpattern = args.file.readline
    else:
        nextpattern = functools.partial(six.moves.input, "Enter a pattern to validate: ")

    try:
        while True:
            pattern = nextpattern()
            if not pattern:
                break
            tests_passed, err_strings = validate(pattern, True)

            if tests_passed:
                print("\nPASS: %s" % pattern)
                pass_count += 1

            else:
                for err in err_strings:
                    print(err, '\n')
                fail_count += 1
    except (EOFError, KeyboardInterrupt):
        pass
    finally:
        if args.file:
            args.file.close()

    print("\nPASSED:", pass_count, " patterns")
    print("FAILED:", fail_count, " patterns")


if __name__ == '__main__':
    main()
