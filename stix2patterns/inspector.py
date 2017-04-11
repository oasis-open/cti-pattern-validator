import antlr4
import antlr4.error.ErrorListener
import collections
import six

from stix2patterns.grammars.STIXPatternListener import STIXPatternListener
from stix2patterns.grammars.STIXPatternLexer import STIXPatternLexer
from stix2patterns.grammars.STIXPatternParser import STIXPatternParser


class MatcherErrorListener(antlr4.error.ErrorListener.ErrorListener):
    """
    Simple error listener which just remembers the last error message received.
    """
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.error_message = u"{}:{}: {}".format(line, column, msg)


class InspectionException(Exception):
    """Represents a error that occurred during inspection."""
    pass


class ParseException(Exception):
    """Represents a parse error."""
    pass


_PatternData = collections.namedtuple("pattern_data",
                                      "comparisons observation_ops qualifiers")


class InspectionListener(STIXPatternListener):
    """This listener collects info about a pattern and puts it
    in a python structure.  It is intended to assist apps which wish to
    look "inside" a pattern and know what's in there.
    """

    def __init__(self):
        self.__comparison_data = {}
        self.__qualifiers = set()
        self.__observation_ops = set()

    def pattern_data(self):
        return _PatternData(self.__comparison_data, self.__observation_ops,
                            self.__qualifiers)

    def __add_prop_tuple(self, obj_type, obj_path, op, value):
        if obj_type not in self.__comparison_data:
            self.__comparison_data[obj_type] = []

        self.__comparison_data[obj_type].append((obj_path, op, value))

    def exitObservationExpressions(self, ctx):
        if ctx.FOLLOWEDBY():
            self.__observation_ops.add(u"FOLLOWEDBY")

    def exitObservationExpressionOr(self, ctx):
        if ctx.OR():
            self.__observation_ops.add(u"OR")

    def exitObservationExpressionAnd(self, ctx):
        if ctx.AND():
            self.__observation_ops.add(u"AND")

    def exitStartStopQualifier(self, ctx):
        self.__qualifiers.add(
            u"START {0} STOP {1}".format(
                ctx.StringLiteral(0), ctx.StringLiteral(1)
            )
        )

    def exitWithinQualifier(self, ctx):
        self.__qualifiers.add(
            u"WITHIN {0} SECONDS".format(
                ctx.IntLiteral() or ctx.FloatLiteral()
            )
        )

    def exitRepeatedQualifier(self, ctx):
        self.__qualifiers.add(
            u"REPEATS {0} TIMES".format(
                ctx.IntLiteral()
            )
        )

    def exitPropTestEqual(self, ctx):
        op_tok = ctx.EQ() or ctx.NEQ()
        op_str = op_tok.getText()

        value = ctx.primitiveLiteral().getText()

        self.__add_prop_tuple(self.__obj_type, self.__obj_path, op_str,
                              value)

    def exitPropTestOrder(self, ctx):
        op_tok = ctx.GT() or ctx.LT() or ctx.GE() or ctx.LE()
        op_str = op_tok.getText()

        value = ctx.orderableLiteral().getText()

        self.__add_prop_tuple(self.__obj_type, self.__obj_path, op_str,
                              value)

    def exitPropTestSet(self, ctx):
        op_str = u"NOT " if ctx.NOT() else u""
        op_str += u"IN"

        value = ctx.setLiteral().getText()

        self.__add_prop_tuple(self.__obj_type, self.__obj_path, op_str,
                              value)

    def exitPropTestLike(self, ctx):
        op_str = u"NOT " if ctx.NOT() else u""
        op_str += u"LIKE"

        value = ctx.StringLiteral().getText()

        self.__add_prop_tuple(self.__obj_type, self.__obj_path, op_str,
                              value)

    def exitPropTestRegex(self, ctx):
        op_str = u"NOT " if ctx.NOT() else u""
        op_str += u"MATCHES"

        value = ctx.StringLiteral().getText()

        self.__add_prop_tuple(self.__obj_type, self.__obj_path, op_str,
                              value)

    def exitPropTestIsSubset(self, ctx):
        op_str = u"NOT " if ctx.NOT() else u""
        op_str += u"ISSUBSET"

        value = ctx.StringLiteral().getText()

        self.__add_prop_tuple(self.__obj_type, self.__obj_path, op_str,
                              value)

    def exitPropTestIsSuperset(self, ctx):
        op_str = u"NOT " if ctx.NOT() else u""
        op_str += u"ISSUPERSET"

        value = ctx.StringLiteral().getText()

        self.__add_prop_tuple(self.__obj_type, self.__obj_path, op_str,
                              value)

    def exitObjectPath(self, ctx):
        path = ctx.getText()

        colon_idx = path.find(u":")
        # shouldn't happen unless the antlr parser failed...
        if colon_idx < 0:
            raise InspectionException(u'Object path didn''t contain ":": {}'
                                      .format(path))

        self.__obj_type = path[:colon_idx]
        self.__obj_path = path[colon_idx+1:]


def get_parse_tree(pattern):
    """
    Match the given pattern against the given observations.  Returns matching
    SDOs.  The matcher can find many bindings; this function returns the SDOs
    corresponding to only the first binding found.

    :param pattern: The STIX pattern
    :return: The parse tree
    """

    in_ = antlr4.InputStream(pattern)
    lexer = STIXPatternLexer(in_)
    lexer.removeErrorListeners()  # remove the default "console" listener
    token_stream = antlr4.CommonTokenStream(lexer)

    parser = STIXPatternParser(token_stream)
    parser.removeErrorListeners()  # remove the default "console" listener
    error_listener = MatcherErrorListener()
    parser.addErrorListener(error_listener)

    # I found no public API for this...
    # The default error handler tries to keep parsing, and I don't
    # think that's appropriate here.  (These error handlers are only for
    # handling the built-in RecognitionException errors.)
    parser._errHandler = antlr4.BailErrorStrategy()

    # To improve error messages, replace "<INVALID>" in the literal
    # names with symbolic names.  This is a hack, but seemed like
    # the simplest workaround.
    for i, lit_name in enumerate(parser.literalNames):
        if lit_name == u"<INVALID>":
            parser.literalNames[i] = parser.symbolicNames[i]

    # parser.setTrace(True)

    try:
        tree = parser.pattern()
        # print(tree.toStringTree(recog=parser))

        return tree
    except antlr4.error.Errors.ParseCancellationException as e:
        # The cancellation exception wraps the real RecognitionException which
        # caused the parser to bail.
        real_exc = e.args[0]

        # I want to bail when the first error is hit.  But I also want
        # a decent error message.  When an error is encountered in
        # Parser.match(), the BailErrorStrategy produces the
        # ParseCancellationException.  It is not a subclass of
        # RecognitionException, so none of the 'except' clauses which would
        # normally report an error are invoked.
        #
        # Error message creation is buried in the ErrorStrategy, and I can
        # (ab)use the API to get a message: register an error listener with
        # the parser, force an error report, then get the message out of the
        # listener.  Error listener registration is above; now we force its
        # invocation.  Wish this could be cleaner...
        parser._errHandler.reportError(parser, real_exc)

        # should probably chain exceptions if we can...
        # Should I report the cancellation or recognition exception as the
        # cause...?
        six.raise_from(ParseException(error_listener.error_message),
                       real_exc)


def inspect_pattern(pattern):
    """Inspect a pattern and pull "stuff" out of it.  The details are TBD."""

    tree = get_parse_tree(pattern)

    inspector = InspectionListener()
    antlr4.ParseTreeWalker.DEFAULT.walk(inspector, tree)

    return inspector.pattern_data()
