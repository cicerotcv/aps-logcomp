%{
#include <stdio.h>

void yyerror(char *c);
int yylex(void);
%}

/* separators */
%token COMMA SEMICOLON

/* special tokens */
%token T_TYPE T_NUMBER T_RETURN T_IDENTIFIER

/* operations */
%token T_PLUS T_MINUS T_MULT T_DIV T_ASSIGN

/* delimiters */
%token OPENING_BRACKET CLOSING_BRACKET 
%token OPENING_CURLY_BRACKET CLOSING_CURLY_BRACKET

/* logical operations */
%token LOG_GT LOG_GE LOG_LT LOG_LE
%token LOG_AND LOG_OR 
%token LOG_EQ LOG_NEQ LOG_NOT

/* reserved words */
%token PRINTF WHILE IF ELSE SCANF


%start TOP_LEVEL

%%
empty: ;

TOP_LEVEL : STATEMENT;


RETURN : T_RETURN ;
NUMBER  : T_NUMBER ;
IDENTIFIER  : T_IDENTIFIER ;

statement_options : empty
                  | IDENTIFIER_DECLARATION
                  | FUNCTION_DEFINITION
                  | FUNCTION_CALL
                  | ASSIGNMENT
                  | BLOCK
                  | WHILE_STATEMENT
                  | IF_STATEMENT 
                  ;

STATEMENT : statement_options SEMICOLON ;

BLOCK : OPENING_CURLY_BRACKET STATEMENT CLOSING_CURLY_BRACKET ;

IDENTIFIER_DECLARATION  : T_TYPE IDENTIFIER ;

function_params : empty
                | T_TYPE IDENTIFIER
                | COMMA function_params
                ;

function_return : RETURN EXPRESSION ;

function_body : OPENING_CURLY_BRACKET STATEMENT CLOSING_CURLY_BRACKET 
              | OPENING_BRACKET STATEMENT function_return CLOSING_CURLY_BRACKET
              ;

FUNCTION_DEFINITION : T_TYPE IDENTIFIER OPENING_BRACKET function_params CLOSING_BRACKET function_body ;

function_args : empty
              | EXPRESSION
              | COMMA function_args
              ;

FUNCTION_CALL : IDENTIFIER OPENING_BRACKET function_args CLOSING_CURLY_BRACKET ;

FACTOR  : NUMBER
        | IDENTIFIER
        | UN_OP FACTOR
        | OPENING_BRACKET CONDITIONAL CLOSING_BRACKET
        ;

TERM  : FACTOR 
      | TERM PRIOR_BIN_OP FACTOR ;

EXPRESSION  : TERM 
            | EXPRESSION BIN_OP TERM ;

CONDITIONAL : EXPRESSION 
            | CONDITIONAL LOGICAL_OP EXPRESSION ;

WHILE_STATEMENT : WHILE OPENING_BRACKET CONDITIONAL CLOSING_BRACKET BLOCK ;

IF_STATEMENT  : IF OPENING_BRACKET CONDITIONAL CLOSING_BRACKET BLOCK ELSE BLOCK
              | IF OPENING_BRACKET CONDITIONAL CLOSING_BRACKET BLOCK
              ;

ASSIGNMENT  : IDENTIFIER T_ASSIGN EXPRESSION ;

PRIOR_BIN_OP  : T_MULT
              | T_DIV
              | LOG_AND
              ;

BIN_OP  : T_MINUS
        | T_PLUS
        | LOG_OR
        ;

UN_OP : LOG_NOT 
      | T_MINUS
      | T_PLUS
      ;

LOGICAL_OP  : LOG_AND
            | LOG_OR
            | LOG_EQ
            | LOG_NEQ
            | LOG_GE
            | LOG_GT
            | LOG_LE
            | LOG_LT
            ;

%%

void yyerror(char *c) {
    printf("Erro: %s\n", c);
}

int main() {
    yyparse();
    return 0;
}