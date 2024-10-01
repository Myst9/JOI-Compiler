grammar joi;

options {
    language = Python3;
}

// Lexer rules (Tokens)
INT: 'int';
MAIN: 'joi';
RETURN: 'return';
INCLUDE: '#include';
IOSTREAM: '<iostream>';
USING: 'using';
NAMESPACE: 'namespace';
STD: 'std';
COUT: 'cout';
CIN: 'cin';
ENDL: 'endl';
LT: '<<';
GT: '>>';
COMMENT: '##' ~[\r\n]* -> skip; // Comment skipping
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' .*? '"';
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip; // Whitespace skipping

// Parser rules
program: includeStmt usingStmt mainFunction EOF;

includeStmt: INCLUDE IOSTREAM;

usingStmt: USING NAMESPACE STD ';';

mainFunction: INT MAIN '(' ')' '{' statements RETURN NUMBER ';' '}';

statements: statement*;

statement
    : printStmt
    | inputStmt
    | assignStmt
    ;

printStmt: COUT LT printExpressionList (LT ENDL)? ';'; // Optional endl

printExpressionList: expression (LT expression)*;

inputStmt: CIN GT IDENTIFIER ';';

assignStmt: IDENTIFIER '=' expression ';';

expression
    : STRING
    | IDENTIFIER
    | NUMBER
    ;

// Entry point for parsing
main: program;
