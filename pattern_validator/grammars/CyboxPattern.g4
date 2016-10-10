grammar CyboxPattern;

startExpression
    :   objectExpression EOF
    ;

objectExpression
    :   left=objectExpression bop=( AND | OR | ALONGWITH | FOLLOWEDBY ) right=objectExpression
    |   (NOT)? LPAREN be=objectExpression RPAREN
    |   (NOT)? booleanExpression
    |   objectExpression (window=timeWindow)
    ;

timeWindow
    :   START startTime=Timestamp (STOP stopTime=Timestamp)?
    |   WITHIN timespec=IntegerLiteral (MILLISECONDS|SECONDS|MINUTES|HOURS|DAYS|MONTHS|YEARS)
    |   REPEATED repeats=IntegerLiteral TIMES
    ;

booleanExpression
    :   expression booleanOperator
    |   cidrExpression
    ;

cidrExpression     
    :   cidrLiteral CONTAINS cidrLiteral
    ;

booleanOperator
    :   comparisonOperator | likeOperator | inOperator | regexOperator;

comparisonOperator : cop=(EQ | NEQ | LT | LE | GT | GE) expression ;

likeOperator       : LIKE pattern=expression ;

regexOperator	   : REGEX regexLiteral;

inOperator         : IN LPAREN (expressionList) RPAREN;

expressionList
    :   thisexpr+=expression (COMMA thisexpr+=expression)*
    ;

expression
    :   literal
    |   objectPath
    |   LPAREN expression arithmeticOperator RPAREN
    |   expression arithmeticOperator
    ;

arithmeticOperator
    :   op = POWER_OP expression
    |   op = ASTERISK expression
    |   op = DIVIDE expression
    |   op = PLUS expression
    |   op = MINUS expression
    |   op = MODULO expression
    ;

arguments
    :   args+=expression (COMMA args+=expression)*
    ;

cidrLiteral
    :   stringLiteral
    |   objectPath
    ;

regexLiteral
    :   RegexLiteral
    ;

RegexLiteral
    :   DIVIDE ( ~'/' | '\'\'' )* DIVIDE
    ;

literal
    :   signedInt
    |   signedFloat
    |   stringLiteral
    |   boolLiteral
    |   binary
    |   NULL
    ;

signedInt
    :   (PLUS|MINUS)?IntegerLiteral         #LiteralInteger
    ;

signedFloat
    :   (PLUS|MINUS)?FloatingPointLiteral   #LiteralFloat
    ;

stringLiteral
    :   StringLiteral
    ;

boolLiteral
    :   (TRUE|FALSE)                        #LiteralBoolean
    ;

binary
    :   Binary
    ;

//////////////////////////////////////////////
// Keywords

AND:  A N D;
ALONGWITH:  A L O N G W I T H ;
OR:  O R;
NOT:  N O T;
FOLLOWEDBY:  F O L L O W E D B Y ;
LIKE:  L I K E ;
REGEX:  M A T C H E S ;
CONTAINS:  C O N T A I N S ;
LAST:  L A S T ;
IN:  I N;
START:  S T A R T ;
STOP:  S T O P ;
MILLISECONDS:  M I L L I S E C O N D S;
SECONDS:  S E C O N D S;
MINUTES:  M I N U T E S;
HOURS:  H O U R S;
DAYS:  D A Y S;
MONTHS:  M O N T H S;
YEARS:  Y E A R S;
TRUE:  T R U E;
FALSE:  F A L S E;
NULL:  N U L L;

WITHIN:  W I T H I N;
REPEATED:  R E P E A T E D;
TIMES:  T I M E S;

// Timestamp syntax based on Stix 2.0 Timestamp
Timestamp
    :   QUOTE Date Time QUOTE
    ;

Date
    :   Year HYPHEN Month HYPHEN Day 'T'
    ;

Time
    :   Hours COLON Minutes COLON Seconds 'Z'
    ;

fragment
Year
    :   [1-2] [0-1] Digit Digit
    ;

fragment
Month
    :   '0' NonZeroDigit
    |   '1' [0-2]
    ;

fragment
Day
    :   '0' NonZeroDigit
    |   [1-2] Digit
    |   '3' [0-1]
    ;

fragment
Hours
    :   [0-1] Digit
    |   '2' [0-3]
    ;

fragment
Seconds
    :   Minutes DOT Digits
    ;

fragment
Minutes
    :   [0-5] Digit
    ;

IntegerLiteral
    :   DecimalNumeral
    ;

FloatingPointLiteral
    :   DecimalFloatingPointLiteral
    ;

fragment
DecimalFloatingPointLiteral
    :   Digits DOT Digits? ExponentPart?
    |   DOT Digits ExponentPart?
    |   Digits ExponentPart
    |   Digits
    ;

fragment
DecimalNumeral
    :   '0'
    |   NonZeroDigit (Digits)?
    ;

fragment
Digits
    :   Digit+
    ;

fragment
Digit
    :   '0'
    |   NonZeroDigit
    ;

fragment
NonZeroDigit
    :   [1-9]
    ;

fragment
ExponentPart
    :   ExponentIndicator SignedInteger
    ;

fragment
ExponentIndicator
    :   [eE]
    ;

fragment
SignedInteger
    :   Sign? Digits
    ;

fragment
Sign
    :   [+-]
    ;

Binary
    :   QUOTE [0-1]+ QUOTE
    ;

StringLiteral
    :   QUOTE ( ~'\'' | '\'\'' )* QUOTE
    ;

fragment
StringCharacters
    :   StringCharacter+
    ;

fragment
StringCharacter
    :   ~['\\]
    ;

fragment
Letter
    :   [a-zA-Z$_]
    ;

fragment
LetterOrDigit
    :   [a-zA-Z0-9$_]
    ;

objectPath
    :   nestedObject
    |   listObject
    |   extObject
    |   simpleObject
    ;

extObject
    :   simpleObject LBRACK StringLiteral RBRACK DOT Identifier
    ;

listObject
    :   simpleObjectList
    |   nestedObjectList
    |   simpleObjectList ((DOT Identifier) | indexObject)+
    |   nestedObjectList ((DOT Identifier) | indexObject)+
    ;

simpleObjectList
    :   simpleObject indexObject
    ;

nestedObjectList
    :   nestedObject indexObject
    ;

nestedObject
    :   simpleObject (DOT Identifier)+
    ;

indexObject
    :   LBRACK (IntegerLiteral | ASTERISK) RBRACK
    ;

simpleObject
    :   Identifier COLON Identifier
    |   ASTERISK COLON Identifier
    ;

Identifier
    :   '"' (~'"' | '""')* '"'
    |   IdentifierChunk+
    ;

IdentifierChunk
    :   [a-zA-Z_0-9]+ HYPHEN?
    ;

EQ        :   '=';
NEQ       :   '!=';
LT        :   '<';
LE        :   '<=';
GT        :   '>';
GE        :   '>=';

QUOTE     : '\'';
SEMI      : ';' ;
COLON     : ':' ;
DOT       : '.' ;
COMMA     : ',' ;
RPAREN    : ')' ;
LPAREN    : '(' ;
RBRACK    : ']' ;
LBRACK    : '[' ;
PLUS      : '+' ;
MINUS     : '-' ;
HYPHEN    : MINUS ;
NEGATION  : '~' ;
VERTBAR   : '|' ;
BITAND    : '&' ;
MODULO    : '%' ;
POWER_OP  : '^' ;
DIVIDE    : '/' ;
ASTERISK  : '*';

fragment A:  [aA];
fragment B:  [bB];
fragment C:  [cC];
fragment D:  [dD];
fragment E:  [eE];
fragment F:  [fF];
fragment G:  [gG];
fragment H:  [hH];
fragment I:  [iI];
fragment J:  [jJ];
fragment K:  [kK];
fragment L:  [lL];
fragment M:  [mM];
fragment N:  [nN];
fragment O:  [oO];
fragment P:  [pP];
fragment Q:  [qQ];
fragment R:  [rR];
fragment S:  [sS];
fragment T:  [tT];
fragment U:  [uU];
fragment V:  [vV];
fragment W:  [wW];
fragment X:  [xX];
fragment Y:  [yY];
fragment Z:  [zZ];

// Whitespace and comments
//
WS  :  [ \t\r\n\u000C]+ -> skip
    ;

COMMENT
    :   '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;
