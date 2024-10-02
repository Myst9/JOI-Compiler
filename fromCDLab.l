
digit [0-9]
number {digit}+
letter [a-z_A-Z]
variable {letter}({digit}|{letter})*
%%


"++" {return DOUBLEPLUS;}
"--" {return DOUBLEMINUS;}
"==" {return DOUBLEEQUAL;}
"!=" {return NOTEQUAL;}
"!"  {return NOT;}
"&&" {return AND;}
"||" {return OR;}
"<=" {return LESSTHANOREQUALTO;}
">=" {return GREATERTHANOREQUALTO;}
"<"  {return LESSTHAN;}
">" {return GREATERTHAN;}
"=" {return EQUALS;}
":" {return COLON;}
{number}"."{number} {return FLOAT;}
{number} {return POSNUMBER;}
"if" {return IF;}
"while" {return WHILE;}
"else" {return ELSE;}
"switch" {return SWITCH;}
"case" {return CASE;}
"default" {return DEFAULT;}
"break" {return BREAK;}
"true" {return BOOLTRUE;}
"false" {return BOOLFALSE;}
"int" {return INTTYPE;}
"char" {return CHARTYPE;}
"float" {return FLOATTYPE;}
"," {return COMMA;}

"+" {return PLUS;}
"-" {return MINUS;}
"*" {return MUL;}
"/" {return DIV;}
"^" {return POW;}
";" {return SEP;}
"(" {return OPENB;}
")" {return CLOSEB;}
"{" {return OPENCB;}
"}" {return CLOSECB;}
"[" {return OPENSB;}
"]" {return CLOSESB;}
{variable} {return VARIABLE;}
" "|"\n"|"\t" {}

. {return yytext[0]; 
}

%%



