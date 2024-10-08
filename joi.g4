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
VOID: 'void';
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
CONTINUE: 'continue';
WHILE: 'while';
DO: 'do';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';
STRUCT: 'struct';
ENUM: 'enum';


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
INC: '++';
DEC: '--';
COLON: ':';
AMPERSAND: '&';
COMMENT: '##' ~[\r\n]* -> skip; 
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
CHAR_LITERAL: '\'' . '\''; // Char literals like 'a'
STRING: '"' (~["\\] | '\\' .)* '"'; 
NUMBER: [0-9]+ ('.' [0-9]+)?; 
WS: [ \t\r\n]+ -> skip;

// Parser rules
program: includeStmt usingStmt functionDefOrStructDefOrEnumDef* mainFunction EOF;

includeStmt: INCLUDE IOSTREAM;

usingStmt: USING NAMESPACE STD ';';

functionDefOrStructDefOrEnumDef: functionDef | structDef | enumDef;

functionDef: (dataType | VOID) IDENTIFIER '(' paramList? ')' COLON statements returnStmt? COLON;

paramList: param (',' param)*;
param: dataType IDENTIFIER;

functionCall: IDENTIFIER '(' argList? ')';

argList: expression (',' expression)*;

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
    | breakStmt
    | continueStmt
    | functionCall ';'
    | expression ';'
    ;


structDef: STRUCT IDENTIFIER COLON declarationStmt+ COLON ;

enumDef: ENUM IDENTIFIER COLON IDENTIFIER (',' IDENTIFIER)* COLON ;

breakStmt: BREAK ';';
continueStmt: CONTINUE ';';
printStmt: COUT LT printExpressionList (LT ENDL)? ';'; 

printExpressionList: expression (LT expression)*;

inputStmt: CIN GT IDENTIFIER ';';

assignStmt: IDENTIFIER '=' expression ';'
            | IDENTIFIER '[' expression ']'('['expression']')* '=' expression ';'
            | structAssignStmt
            ;

structAssignStmt: structAccessStmt '=' expression ';'
                | structAccessStmt '[' expression ']'('['expression']')* '=' expression ';'
                ;

structAccessStmt: IDENTIFIER'.'IDENTIFIER;

returnStmt: RETURN expression ';';

declarationStmt: dataType varList ('=' expression)? ';'
                | arrayDeclarationStmt ';'
                | referenceDeclarationStmt ';'
                ; 

arrayDeclarationStmt: dataType IDENTIFIER '[' expression ']' ('['expression']')* ('=' arrayValueAssigning)? ;

arrayValueAssigning: '{'arrayValueAssigning (',' arrayValueAssigning)*'}' | expression;

referenceDeclarationStmt: referenceDataType IDENTIFIER '=' IDENTIFIER ('['expression']')*
                        ;

constDeclarationStmt: CONST declarationStmt;

varList: IDENTIFIER (',' IDENTIFIER)*;

ifStmt
    : IF condition COLON '{' statements '}' (elseIfStmt* elseStmt?)? ;

elseIfStmt
    : ELSE IF condition COLON '{' statements '}' ;

elseStmt
    : ELSE COLON '{' statements '}' ;

switchStmt: SWITCH expression COLON '{' caseStmt* defaultStmt? '}';

caseStmt: CASE expression ':' statements BREAK ';';

defaultStmt: DEFAULT ':' statements;

whileStmt: WHILE condition COLON '{' statements '}';

doWhileStmt: DO '{' statements '}' WHILE  condition COLON ;

forStmt: FOR forInit condition? ';' forUpdate ':' '{' statements '}';



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
    | INC IDENTIFIER
    | DEC IDENTIFIER
    | IDENTIFIER INC
    | IDENTIFIER DEC
    ;

expression
    : logicalOrExpression
    | functionCall
    ;

logicalOrExpression
    : logicalAndExpression (OR logicalAndExpression)*
    ;

logicalAndExpression
    : rel_expr (AND rel_expr)*
    ;

rel_expr
    : NOT rel_expr
    | expr (comparisonOp expr)*
    ;

expr
    : term ((ADD | SUB) term)*
    ;

term
    : factor ((MUL | DIV | MOD) factor)*
    ;

factor
    : INC IDENTIFIER
    | DEC IDENTIFIER
    | IDENTIFIER INC
    | IDENTIFIER DEC
    | STRING
    | CHAR_LITERAL
    | IDENTIFIER
    | NUMBER
    | IDENTIFIER ('[' expr ']')+
    | '(' expr ')'
    | TRUE
    | FALSE
    | structAccessStmt
    ;

// Expressions and conditions

condition: expression;

arithmeticOp: ADD | SUB | MUL | DIV | MOD;

comparisonOp: EQ | NEQ | GT_OP | LT_OP | GTE | LTE;

logicalOp: AND | OR;

// Data types
dataType: INT | BOOL | FLOAT | CHAR | STR ;
referenceDataType: INT AMPERSAND| BOOL AMPERSAND | FLOAT AMPERSAND | CHAR AMPERSAND | STR AMPERSAND; 

// Entry point for parsing
main: program;
