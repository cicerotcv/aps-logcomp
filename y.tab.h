/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    COMMA = 258,
    SEMICOLON = 259,
    T_TYPE = 260,
    T_NUMBER = 261,
    T_RETURN = 262,
    T_IDENTIFIER = 263,
    T_PLUS = 264,
    T_MINUS = 265,
    T_MULT = 266,
    T_DIV = 267,
    T_ASSIGN = 268,
    OPENING_BRACKET = 269,
    CLOSING_BRACKET = 270,
    OPENING_CURLY_BRACKET = 271,
    CLOSING_CURLY_BRACKET = 272,
    LOG_GT = 273,
    LOG_GE = 274,
    LOG_LT = 275,
    LOG_LE = 276,
    LOG_AND = 277,
    LOG_OR = 278,
    LOG_EQ = 279,
    LOG_NEQ = 280,
    LOG_NOT = 281,
    PRINTF = 282,
    WHILE = 283,
    IF = 284,
    ELSE = 285,
    SCANF = 286
  };
#endif
/* Tokens.  */
#define COMMA 258
#define SEMICOLON 259
#define T_TYPE 260
#define T_NUMBER 261
#define T_RETURN 262
#define T_IDENTIFIER 263
#define T_PLUS 264
#define T_MINUS 265
#define T_MULT 266
#define T_DIV 267
#define T_ASSIGN 268
#define OPENING_BRACKET 269
#define CLOSING_BRACKET 270
#define OPENING_CURLY_BRACKET 271
#define CLOSING_CURLY_BRACKET 272
#define LOG_GT 273
#define LOG_GE 274
#define LOG_LT 275
#define LOG_LE 276
#define LOG_AND 277
#define LOG_OR 278
#define LOG_EQ 279
#define LOG_NEQ 280
#define LOG_NOT 281
#define PRINTF 282
#define WHILE 283
#define IF 284
#define ELSE 285
#define SCANF 286

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
