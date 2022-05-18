%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "json2.tab.h"

int line;

%}
DIGIT [0-9]
DIGITS {DIGIT}+
ALPARITHMITIKA [a-zA-Z_]

FLOAT [.]{DIGITS}
EXPONAL {EX}{DIGITS}
EX [eE][+-]?
HEX_DIGIT [0-9a-f]
ALL_CHARS [ -!#-\[\]-~]
BRAKES_CHARS \\["\\bfnrt/]
UNICODECHAR \\u{HEX_DIGIT}{HEX_DIGIT}{HEX_DIGIT}{HEX_DIGIT}
CHAR {ALL_CHARS}|{BRAKES_CHARS}|{UNICODECHAR} 

STR {CHAR}+
DBL_QUOT ["]	
%%

Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec		{printf("%s",yytext); return MONTH;}
Mon|Thu|Wed|Tue|Fri|Sat|Sun							{ printf("%s", yytext); return DAY;}
true										{printf("%s", yytext); return TRUE; }
false										{printf("%s", yytext); return FALSE; }

 {DBL_QUOT}text{DBL_QUOT} 					{printf("%s", yytext); return TEXT; }	
 {DBL_QUOT}user{DBL_QUOT} 					{printf("%s", yytext); return USER; }
 {DBL_QUOT}location{DBL_QUOT} 				{printf("%s", yytext); return LOCATION; }
 
 {DBL_QUOT}url{DBL_QUOT} 				{printf("%s", yytext); return URL; }
 {DBL_QUOT}description{DBL_QUOT} 				{printf("%s", yytext); return DESCRIPTION1; }
 
 {DBL_QUOT}name{DBL_QUOT} 					{printf("%s", yytext); return NAME; }
 {DBL_QUOT}screen_name{DBL_QUOT} 				{printf("%s", yytext); return SCREEN_NAME1; }
 {DBL_QUOT}id_str{DBL_QUOT} 					{printf("%s", yytext); return ID_STR; }
 {DBL_QUOT}id{DBL_QUOT} 						{printf("%s", yytext); return ID; }
 {DBL_QUOT}created_at{DBL_QUOT} 				{printf("%s", yytext); return CREATED_AT; }
 {DBL_QUOT}RT@{DBL_QUOT} 		{printf("%s", yytext); return RTWET_STS; }
 {DBL_QUOT}tweet{DBL_QUOT} 					{printf("%s", yytext); return TWEET; }
 {DBL_QUOT}extended_tweet{DBL_QUOT} 			{printf("%s", yytext); return EXTENDED_TWEET; }



\{		{printf("{"); return '{';}
\}		{printf("}"); return '}';}
{DBL_QUOT} 		{printf(" \n "); return QUOT;}
,		{printf(","); return ',';}
:		{printf(":"); return ':';}

	
 {DBL_QUOT}{DIGITS}{DBL_QUOT} 		{printf("%s", yytext); return QUT_INTEGERBER; }
 {DBL_QUOT}{STR}{DBL_QUOT} 		{printf("%s", yytext); return STRING; }	
{DIGITS}		{printf("%s", yytext); return INTEGER; }

\n { printf("%s",yytext); line++; }  
[ ] 	{printf("%s",yytext);};
[\t] 	{printf("%s",yytext);};
%%
