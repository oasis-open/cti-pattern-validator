# Generated from PCRE.g4 by ANTLR 4.6
from antlr4 import *

# This class defines a complete listener for a parse tree produced by PCREParser.
class PCREListener(ParseTreeListener):

    # Enter a parse tree produced by PCREParser#alternation.
    def enterAlternation(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#alternation.
    def exitAlternation(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#pcreexpr.
    def enterPcreexpr(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#pcreexpr.
    def exitPcreexpr(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#element.
    def enterElement(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#element.
    def exitElement(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#quantifier.
    def enterQuantifier(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#quantifier.
    def exitQuantifier(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#quantifier_type.
    def enterQuantifier_type(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#quantifier_type.
    def exitQuantifier_type(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#character_class.
    def enterCharacter_class(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#character_class.
    def exitCharacter_class(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#backreference.
    def enterBackreference(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#backreference.
    def exitBackreference(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#backreference_or_octal.
    def enterBackreference_or_octal(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#backreference_or_octal.
    def exitBackreference_or_octal(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#capture.
    def enterCapture(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#capture.
    def exitCapture(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#non_capture.
    def enterNon_capture(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#non_capture.
    def exitNon_capture(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#comment.
    def enterComment(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#comment.
    def exitComment(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#option.
    def enterOption(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#option.
    def exitOption(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#option_flags.
    def enterOption_flags(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#option_flags.
    def exitOption_flags(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#option_flag.
    def enterOption_flag(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#option_flag.
    def exitOption_flag(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#look_around.
    def enterLook_around(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#look_around.
    def exitLook_around(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#subroutine_reference.
    def enterSubroutine_reference(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#subroutine_reference.
    def exitSubroutine_reference(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#conditional.
    def enterConditional(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#conditional.
    def exitConditional(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#backtrack_control.
    def enterBacktrack_control(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#backtrack_control.
    def exitBacktrack_control(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#newline_convention.
    def enterNewline_convention(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#newline_convention.
    def exitNewline_convention(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#callout.
    def enterCallout(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#callout.
    def exitCallout(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#atom.
    def enterAtom(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#atom.
    def exitAtom(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#cc_atom.
    def enterCc_atom(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#cc_atom.
    def exitCc_atom(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#shared_atom.
    def enterShared_atom(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#shared_atom.
    def exitShared_atom(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#pcre_literal.
    def enterPcre_literal(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#pcre_literal.
    def exitPcre_literal(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#cc_literal.
    def enterCc_literal(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#cc_literal.
    def exitCc_literal(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#shared_literal.
    def enterShared_literal(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#shared_literal.
    def exitShared_literal(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#number.
    def enterNumber(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#number.
    def exitNumber(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#octal_char.
    def enterOctal_char(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#octal_char.
    def exitOctal_char(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#octal_digit.
    def enterOctal_digit(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#octal_digit.
    def exitOctal_digit(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#digits.
    def enterDigits(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#digits.
    def exitDigits(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#digit.
    def enterDigit(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#digit.
    def exitDigit(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#name.
    def enterName(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#name.
    def exitName(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#alpha_nums.
    def enterAlpha_nums(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#alpha_nums.
    def exitAlpha_nums(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#non_close_parens.
    def enterNon_close_parens(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#non_close_parens.
    def exitNon_close_parens(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#non_close_paren.
    def enterNon_close_paren(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#non_close_paren.
    def exitNon_close_paren(self, ctx):
        pass


    # Enter a parse tree produced by PCREParser#letter.
    def enterLetter(self, ctx):
        pass

    # Exit a parse tree produced by PCREParser#letter.
    def exitLetter(self, ctx):
        pass


