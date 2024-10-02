grammar joi;

options {
    language = Python3;
}

// Lexer rules (Tokens)
INT: 'int';
BOOL: 'bool';
FLOAT: 'float';
CHAR: 'char';
STR: 'str';
CONST: 'constant';
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
IF: 'if';
ELSE: 'else';
SWITCH: 'switch';
CASE: 'case';
DEFAULT: 'default';
BREAK: 'break';
WHILE: 'while';
DO: 'do';
FOR: 'for';
EQ: '==';
NEQ: '!=';
GT_OP: '>';
LT_OP: '<';
GTE: '>='; 
LTE: '<=';
AND: '&&';
OR: '||';
NOT: '!';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
COMMENT: '##' ~[\r\n]* -> skip; 
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
CHAR_LITERAL: '\'' . '\''; // Char literals like 'a'
STRING: '"' (~["\\] | '\\' .)* '"'; 
NUMBER: [0-9]+ ('.' [0-9]+)?; 
WS: [ \t\r\n]+ -> skip;

// Parser rules
program: includeStmt usingStmt mainFunction EOF;

includeStmt: INCLUDE IOSTREAM;

usingStmt: USING NAMESPACE STD ';';

mainFunction: INT MAIN '(' ')' '{' statements RETURN expression ';' '}';

statements: statement*;

statement
    : printStmt
    | inputStmt
    | assignStmt
    | declarationStmt
    | constDeclarationStmt
    | ifStmt
    | switchStmt
    | whileStmt
    | doWhileStmt
    | forStmt
    | returnStmt
    ;

printStmt: COUT LT printExpressionList (LT ENDL)? ';'; 

printExpressionList: expression (LT expression)*;

inputStmt: CIN GT IDENTIFIER ';';

assignStmt: IDENTIFIER '=' expression ';';

returnStmt: RETURN expression ';';

declarationStmt: dataType varList ('=' expression)? ';'; 

constDeclarationStmt: CONST dataType IDENTIFIER '=' expression ';';

varList: IDENTIFIER (',' IDENTIFIER)*;

ifStmt: IF '(' condition ')' '{' statements '}' (ELSE '{' statements '}')?;

switchStmt: SWITCH '(' expression ')' '{' caseStmt* defaultStmt? '}';

caseStmt: CASE expression ':' statements BREAK ';';

defaultStmt: DEFAULT ':' statements;

whileStmt: WHILE '(' condition ')' '{' statements '}';

doWhileStmt: DO '{' statements '}' WHILE '(' condition ')' ';';

forStmt: FOR '(' forInit condition? ';' forUpdate ')' '{' statements '}';

// Define initialization for for loop
forInit
    : assignStmt
    | declarationStmt
    | // Allow multiple initialization statements separated by commas
      declarationStmt (',' declarationStmt)*
    ;

// Define updates for for loop
forUpdate
    : IDENTIFIER '=' expression
    | // Allow multiple update statements separated by commas
      IDENTIFIER '=' expression (',' IDENTIFIER '=' expression)*
    ;

// Expressions and conditions
expression
    : STRING
    | CHAR_LITERAL       
    | IDENTIFIER
    | NUMBER
    | '(' expression ')' 
    | expression arithmeticOp expression
    | expression comparisonOp expression
    | expression logicalOp expression
    | NOT expression      
    | IDENTIFIER '[' expression ']'
    ;

condition: expression;

arithmeticOp: ADD | SUB | MUL | DIV | MOD;

comparisonOp: EQ | NEQ | GT_OP | LT_OP | GTE | LTE;

logicalOp: AND | OR;

// Data types
dataType: INT | BOOL | FLOAT | CHAR | STR;

// Entry point for parsing
main: program;
