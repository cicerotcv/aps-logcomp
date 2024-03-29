%{
#include <stdio.h>
#include <string.h>
%}

%%

","             { return COMMA; }
";"             { return SEMICOLON; }

"$"             { return T_CONCAT; }
"+"             { return T_PLUS; }
"-"             { return T_MINUS; }
"/"             { return T_DIV; }
"*"             { return T_MULT; }
"="             { return T_ASSIGN; }

"("             { return OPENING_BRACKET; }
")"             { return CLOSING_BRACKET; }
"{"             { return OPENING_CURLY_BRACKET; }
"}"             { return CLOSING_CURLY_BRACKET; }

">"                       { return LOG_GT; }
">="                      { return LOG_GE; }
"<"                       { return LOG_LT; }
"<="                      { return LOG_LE; }
"and"                     { return LOG_AND; }
"not"                     { return LOG_NOT; }
"or"                      { return LOG_OR; }
"=="                      { return LOG_EQ; }
"!="                      { return LOG_NEQ; }

"stdout"                  { return PRINTF; }
"while"                   { return WHILE; }
"if"                      { return IF; }
"else"                    { return ELSE; }
"stdin"                   { return SCANF; }


["int" | "str" | "void"]  { return T_TYPE; }
[1-9][0-9]*               { return T_NUMBER; }
"return"                  { return T_RETURN; }
[A-z_][0-9A-z_]+          { return T_IDENTIFIER; }


%%
