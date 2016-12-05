'''
Validates a user entered pattern against CyboxPattern and PCRE grammars.
'''

from __future__ import print_function
import argparse

from antlr4 import InputStream
from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
import six

from .grammars.CyboxPatternLexer import CyboxPatternLexer
from .grammars.CyboxPatternParser import CyboxPatternParser
from .grammars.CyboxPatternListener import CyboxPatternListener
from .grammars.PCRELexer import PCRELexer
from .grammars.PCREParser import PCREParser


class CyboxPatternErrorListener(ErrorListener):
    '''
    Modifies ErrorListener to collect error message and set flag to False when
    invalid pattern is encountered.
    '''
    def __init__(self):
        super(CyboxPatternErrorListener, self).__init__()
        self.err_strings = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.err_strings.append("FAIL: Error found at line %d:%d. %s" %
                                (line, column, msg))


class PCREErrorListener(ErrorListener):
    '''
    Modifies ErrorListener for PCRE to collect a more appropriate error
    message.
    '''
    def __init__(self):
        super(PCREErrorListener, self).__init__()
        self.err_strings = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.err_strings.append("FAIL: Regex error found. %s." % msg)


class REGEXValidatorListener(CyboxPatternListener):
    """
    A parser listener which triggers when the parse process encounters regex
    literals.  This listener will validate the regexes and collect error
    messages into a list.
    """
    def __init__(self):
        self.err_strings = []

    def exitRegexLiteral(self, ctx):
        # returns a TerminalNode; we need the actual token string
        regex = str(ctx.RegexLiteral())

        # strip leading/trailing "/"
        in_ = InputStream(regex[1:-1])
        lexer = PCRELexer(in_)
        lexer.removeErrorListeners()
        stream = CommonTokenStream(lexer)
        pcre_parser = PCREParser(stream)
        pcre_parser.buildParseTrees = False
        pcre_parser.removeErrorListeners()
        errListener = PCREErrorListener()
        pcre_parser.addErrorListener(errListener)
        pcre_parser.alternation()

        self.err_strings.extend(err + ' REGEX: ' + regex
                                for err in errListener.err_strings)


def run_validator(pattern):
    '''
    Validates a pattern against the CybOX grammar.  Error messages are
    returned in a list.  The test passed if the returned list is empty.
    '''

    if isinstance(pattern, six.string_types):
        pattern = InputStream(pattern)

    parseErrListener = CyboxPatternErrorListener()

    lexer = CyboxPatternLexer(pattern)
    # it always adds a console listener by default... remove it.
    lexer.removeErrorListeners()

    stream = CommonTokenStream(lexer)

    parser = CyboxPatternParser(stream)
    parser.buildParseTrees = False
    # it always adds a console listener by default... remove it.
    parser.removeErrorListeners()
    parser.addErrorListener(parseErrListener)
    regexListener = REGEXValidatorListener()
    parser.addParseListener(regexListener)

    parser.pattern()

    err_strings = parseErrListener.err_strings + regexListener.err_strings

    return err_strings


def validate(user_input, ret_errs=False, print_errs=False):
    '''
    Wrapper for run_validator function that returns True if the user_input
    contains a valid CybOX pattern or False otherwise. The error messages may
    also be returned or printed based upon the ret_errs and print_errs arg
    values.
    '''

    errs = run_validator(user_input)
    passed = len(errs) == 0

    if print_errs:
        for err in errs:
            print(err)

    if ret_errs:
        return passed, errs

    return passed


def main():
    '''
    Continues to validate patterns until it encounters EOF within a pattern
    file or Ctrl-C is pressed by the user.
    '''
    parser = argparse.ArgumentParser(
        description='Validate CybOX Patterns.')
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
        nextpattern = functools.partial(raw_input, "Enter a pattern to validate: ")

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
