%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


FILE *yyin;

void yyerror(const char *s);
extern char* yytext;
extern int line;

%}

%token QUOT
%token STRING
%token INTEGER
%token TEXT
%token MONTH
%token DAY
%token ID_STR
%token QUT_INTEGERBER
%token USER
%token ID
%token NAME
%token SCREEN_NAME1
%token LOCATION
%token URL
%token DESCRIPTION1

%token CREATED_AT
%token RTWET_STS
%token TWEET
%token TRUNCATED
%token EXTENDED_TWEET
%token TRUE
%token FALSE
%token FULL_TEXT
%token DISPLAY_TEXT_RANGE


%%
json_tweet: '{' json_code '}' ;


json_code: 		commands | 
				json_code ',' commands;
commands: 		text|created_at|  id_str 
				|user | fields |RTWET_STS1 
				|  truncated | 
				extended_tweet | tweet;

created_at: 	CREATED_AT ':'  
				DAY MONTH INTEGER INTEGER ':' INTEGER ':' INTEGER  INTEGER  ;

text: 			TEXT ':' STRING ;

				
user: 			USER ':' '{' userjson_code  '}' ;

userjson_code: 	user_commands 
				| userjson_code ',' user_commands;


id_str: 		ID_STR ':' QUT_INTEGERBER  ;

fields: STRING ':' STRING ;

user_commands: 		id | name 
					| screen_name_cmd | location | url | description | fields;
										
id: 			ID ':' INTEGER;

name: 			NAME ':' STRING;

screen_name_cmd: 	SCREEN_NAME1 ':' STRING;

location: LOCATION ':' STRING;

url: URL ':' STRING;

description: DESCRIPTION1 ':' STRING;
 
RTWET_STS1: 			RTWET_STS ':' '{' rtjson_code  '}' ;
rtjson_code: 		text ',' user| user ',' text;
tweet: 				TWEET ':' '{' rtjson_code  '}' ;

truncated: 				TRUNCATED ':' TRUE ',' display_text_range 
						| TRUNCATED ':' FALSE;
extended_tweet: 		EXTENDED_TWEET '{' full_text ',' display_text_range '}';

full_text : 			FULL_TEXT ':' STRING;

display_text_range: 		DISPLAY_TEXT_RANGE ':' array_INTEGER;

array_INTEGER : 		'[' numbers ']';

numbers: INTEGER | numbers ',' INTEGER;

%%

void yyerror(const char *s) {
	printf(" [error !] %d\n",line);
	exit(1);
}

int main(int argc, char* argv[]) {
	FILE *f;
	line=1;
	f = fopen(argv[1], "r");
	yyin = f;
	yyparse();
	printf(" Syndax correct !\n\n\n");	
		
}


