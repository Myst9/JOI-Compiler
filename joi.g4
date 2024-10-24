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
PRIVATE: 'private';
PUBLIC: 'public';
PROTECTED: 'protected';
CLASS: 'class';
VIRTUAL: 'virtual';
NEW: 'new';
DELETE: 'delete';
TRY: 'try';
CATCH: 'catch';
THROW: 'throw';

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
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
COLON: ':';
AMPERSAND: '&';
DOLLAR: '$';
COMMENT: '##' ~[\r\n]* -> skip; 
IDENTIFIER: [a-zA-Z_][a-zA-Z_0-9]*;
CHAR_LITERAL: '\'' . '\''; // Char literals like 'a'
STRING: '"' (~["\\] | '\\' .)* '"'; 
NUMBER: [0-9]+ ('.' [0-9]+)?; 
WS: [ \t\r\n]+ -> skip;

// Parser rules
program: includeStmt usingStmt (functionDefOrStructDefOrEnumDef | declarationStmt | classDef | constDeclarationStmt)* mainFunction EOF; //added declarationStmt* here becuase of global scope and local scope requirement of joi

includeStmt: INCLUDE IOSTREAM;

usingStmt: USING NAMESPACE STD ';';

functionDefOrStructDefOrEnumDef: functionDef | structDef | enumDef;

functionDef: (dataType | VOID) IDENTIFIER '(' paramList? ')' COLON statements returnStmt? COLON;

classDef: CLASS IDENTIFIER (COLON PUBLIC IDENTIFIER (',' PUBLIC IDENTIFIER)*)? COLON (accessSpecifier COLON (declarationStmt|functionDef|constructor)*)* COLON ';';

constructor: IDENTIFIER '(' paramList? ')' COLON statements COLON;

paramList: param (',' param)*;
param: dataType idOrPointerOrAddrId;

functionCall: IDENTIFIER '(' argList? ')'
    | IDENTIFIER '.' IDENTIFIER '(' argList? ')'
    | structAccessStmt '(' argList? ')'
    ;

argList: expression (',' expression)*;

mainFunction: INT MAIN '(' ')' '{' statements RETURN expression ';' '}';

statements: statement*;

statement
    : printStmt
    | inputStmt
    | assignStmt
    | classFunctionAccessStmt
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
    | deleteStmt
    | tryCatchStmt
    | throwStmt
    | objectDeclarationStmt
    | structDeclarationStmt
    ;

deleteStmt: DELETE idOrPointerOrAddrId ';';

structDef: STRUCT IDENTIFIER COLON declarationStmt+ COLON ;

enumDef: ENUM IDENTIFIER COLON IDENTIFIER (',' IDENTIFIER)* COLON ;

breakStmt: BREAK ';';
continueStmt: CONTINUE ';';
printStmt: COUT LT printExpressionList (LT printExpressionList)* ';';

printExpressionList
    : expression
    | ENDL
    ;

inputStmt: CIN GT idOrPointerOrAddrId ';';

assignStmt: idOrPointerOrAddrId '=' expression ';'
            | IDENTIFIER '=' typecastExpr ';'
            | idOrPointerOrAddrId '[' expression ']'('['expression']')* '=' expression ';'
            | idOrPointerOrAddrId assignOp expression ';'
            | structAssignStmt
            ;

structAssignStmt: structAccessStmt '=' expression ';'
                | structAccessStmt '[' expression ']'('['expression']')* '=' expression ';'
                ;



structAccessStmt: IDENTIFIER'.'IDENTIFIER;

structDeclarationStmt: IDENTIFIER IDENTIFIER ';';
objectDeclarationStmt: IDENTIFIER IDENTIFIER '=' NEW IDENTIFIER '('(expression (',' expression)*)?')'';';

classFunctionAccessStmt: IDENTIFIER'.'functionCall';';

returnStmt: RETURN expression ';';

declarationStmt:  dataType varList ('=' expression)? ';'
                | arrayDeclarationStmt ';'
                ; 

arrayDeclarationStmt: dataType idOrPointerOrAddrId '[' expression ']' ('['expression']')* ('=' arrayValueAssigning)? ;

arrayValueAssigning: '{'arrayValueAssigning (',' arrayValueAssigning)*'}' | expression ;

referenceDeclarationStmt: dataType address_identifier '=' idOrPointerOrAddrId ('['expression']')*
                        ;

constDeclarationStmt: CONST declarationStmt;

varList: var (',' var)*;

var: idOrPointerOrAddrId;

tryCatchStmt
    : TRY COLON statements COLON catchBlock+;

catchBlock
    : CATCH '(' IDENTIFIER IDENTIFIER ')' COLON statements COLON;

throwStmt
    : THROW expression ';';

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
    : expression;


accessSpecifier: PRIVATE
                | PUBLIC
                | PROTECTED
                ;

expression
    : logicalOrExpression
    | typecastExpr
    ;

typecastExpr: '(' dataType ')' IDENTIFIER;

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
    : INC idOrPointerOrAddrId
    | DEC idOrPointerOrAddrId
    | idOrPointerOrAddrId INC
    | idOrPointerOrAddrId DEC
    | STRING
    | CHAR_LITERAL
    | idOrPointerOrAddrId
    | NUMBER
    | idOrPointerOrAddrId ('[' expr ']')+
    | '(' expr ')'
    | TRUE
    | FALSE
    | functionCall
    | structAccessStmt
    ;

idOrPointerOrAddrId: IDENTIFIER
                    | pointer
                    | address_identifier;

pointer: DOLLAR idOrPointerOrAddrId;
address_identifier: AMPERSAND IDENTIFIER;

// Expressions and conditions

condition: expression;

arithmeticOp: ADD | SUB | MUL | DIV | MOD;

assignOp: PLUS_ASSIGN | MINUS_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN;

comparisonOp: EQ | NEQ | GT_OP | LT_OP | GTE | LTE;

logicalOp: AND | OR;

// Data types
dataType: INT | BOOL | FLOAT | CHAR | STR ;
referenceDataType: INT AMPERSAND| BOOL AMPERSAND | FLOAT AMPERSAND | CHAR AMPERSAND | STR AMPERSAND; 
// Entry point for parsing
main: program;
