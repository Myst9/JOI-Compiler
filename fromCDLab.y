

%token POSNUMBER FLOAT PLUS MINUS SEP MUL DIV POW OPENB CLOSEB DOUBLEPLUS  DOUBLEMINUS VARIABLE EQUALS IF ELSE OPENCB CLOSECB NOT DOUBLEEQUAL NOTEQUAL LESSTHANOREQUALTO GREATERTHANOREQUALTO LESSTHAN GREATERTHAN BOOLTRUE BOOLFALSE AND OR WHILE SWITCH CASE DEFAULT BREAK COLON INTTYPE FLOATTYPE CHARTYPE COMMA OPENSB CLOSESB
//%type <dval> POSNUMBER
//%type <lexeme> VARIABLE 
%type <Node> E
%type <Node> T
%type <Node> F
%type <Node> K
%type <Node> B
%type <Node> N
%type <Node> I
%type <Node> V
%type <Node> NUME
%type <Node> NUMT
%type <Node> NUMF
%type <Node> NUMK
%type <Node> NUMN
%type <Node> ABCD
%type <Node> RELOP
%type <Node> BOOLOP
%type <Node> BOOLEXPR
%type <Node> BOOL
%type <Node> STMT
%type <Node> STMTS
%type <Node> WHILE //i donot know why but stopped warnings that never affected the output;
%type <Node> IF //i donot know why but stopped warnings that never affected the output;
%type <Node> SWITCH 
%type <Node> CASE
%type <Node> DEFAULT 
%type <Node> BREAK 
%type <Node> VARTYPE 
%type <Node> FURTHERDECLARATION
%type <Node> DECLRSTMT
%type <Node> INTTYPE
%type <Node> CHARTYPE
%type <Node> FLOATTYPE
%nonassoc P
%nonassoc Q
%%

STMTS: STMT SEP 
	| IF OPENB BOOLEXPR CLOSEB OPENCB STMTS CLOSECB  FURTHERIF

	| WHILE OPENB BOOLEXPR CLOSEB OPENCB STMTS CLOSECB STMTS 

	| SWITCH OPENB E CLOSEB OPENCB CASESTMTS CLOSECB STMTS
	| OPENCB STMTS CLOSECB STMTS; 
	|{};

CASESTMTS: CASE NUME COLON STMTS BREAKSTMTFORSWITCH CASESTMTS
	| DEFAULT COLON STMTS
	|
	;

BREAKSTMTFORSWITCH: BREAK SEP | ;

FURTHERIF: ELSE OPENCB STMTS CLOSECB STMTS
	| 	STMTS;


STMT:   VARTYPE FURTHERDECLARATION
	|V EQUALS E 
	|ABCD ;

VARTYPE: INTTYPE 
	|CHARTYPE 
	|FLOATTYPE ;

FURTHERDECLARATION: DECLRSTMT COMMA FURTHERDECLARATION | DECLRSTMT;

DECLRSTMT: V 
	| V EQUALS E
		
	| V INDEX
		;

INDEX: OPENSB I CLOSESB INDEX | OPENSB I CLOSESB ;

E: E PLUS T 
  | E MINUS T 
  | T
  ;


NUME: NUME PLUS NUMT 
  | NUME MINUS NUMT 
  | NUMT{$$ = $1;}
  ;

T: T MUL F 
  | T DIV F 
  | F
  ;

NUMT: NUMT MUL NUMF 
  | NUMT DIV NUMF 
  | NUMF
  ;

F: K POW F 
  | K;

NUMF: NUMK POW NUMF 
  | NUMK;

K: V 
  | I 
  | B 
  | N ;

NUMK: I 
  | NUMN ;

N: ABCD 

  | OPENB E CLOSEB 
  | MINUS OPENB E CLOSEB ; 

NUMN: OPENB NUME CLOSEB 
  | MINUS OPENB NUME CLOSEB ; 

ABCD: DOUBLEPLUS V 
  | DOUBLEMINUS V 

  | V DOUBLEPLUS 

  |V DOUBLEMINUS ;

I: FLOAT
	| POSNUMBER 
	| MINUS POSNUMBER ;

V: VARIABLE
	| MINUS VARIABLE ;
	
B: BOOLTRUE 
	| BOOLFALSE	;

BOOLEXPR: BOOL BOOLOP BOOLEXPR 
	 | BOOL ;

BOOL: E RELOP E 
	| E 
	| OPENB BOOLEXPR CLOSEB 
	| NOT BOOL 
	;

BOOLOP: AND 
	| OR 
	; 

RELOP: LESSTHAN
	| GREATERTHAN 
	| LESSTHANOREQUALTO 
	| GREATERTHANOREQUALTO 
	| DOUBLEEQUAL 
	| NOTEQUAL
	;
%%
