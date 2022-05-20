# -*- errors -*-
E_TOKEN_ERROR = 'invalid_token'
E_SYNTAX_ERROR = 'syntax_error'
E_OPERATION_ERROR = 'operation_error'
E_MISSING_IDENTIFIER = 'missing_identifier'
E_IDENTIFIER_ERROR = 'identifier_error'
E_UNCLOSING_DELIMITER = 'unclosing_delimiter'
E_TYPE_ERROR = 'type_error'

# -*- built-in types -*-
T_INT = 'INT'
T_STR = 'STR'

# -*- operators -*-
OP_PLUS = 'T_PLUS'
OP_MINUS = 'T_MINUS'
OP_MULTI = 'T_MULTI'
OP_DIV = 'T_DIV'
OP_NOT = 'LOG_NOT'
OP_ASSIGNMENT = 'T_ASSIGNMENT'

T_OPENING_CURLY_BRACKET = r'\{'
T_CLOSING_CURLY_BRACKET = r'\}'
T_OPENING_BRACKET = r'\('
T_CLOSING_BRACKET = r'\)'
T_PLUS = r'\+'
T_MINUS = r'\-'
T_MULTI = r'\*'
T_DIV = r'\/'
LOG_OR = r'or'
LOG_AND = r'and'
LOG_EQ = r'(==)'
T_ASSIGNMENT = r'='
LOG_NEQ = r'(!=)'
LOG_NOT = r'!'
LOG_GE = r'(>=)'
LOG_GT = r'(>)'
LOG_LE = r'(<=)'
LOG_LT = r'(<)'
T_COMMENT = r'\/\*.+\*\/'


# -*- delimiters -*-
D_OBRACKET = '('
D_CBRACKET = ')'
D_O_CURLYBRACKET = '{'
D_C_CURLYBRACKET = '}'
D_SEMICOLON = ';'
D_COMMA = ','

# -*- logical operators -*-
LOG_OR = 'logical_or'
LOG_AND = 'logical_and'
LOG_EQ = 'logical_eq'
LOG_GT = 'greater_than'
LOG_LT = 'less_than'

# -*- Reserved words -*-
R_PRINTF = 'printf'
R_SCANF = 'scanf'
R_WHILE = 'while'
R_IF = 'if'
R_ELSE = 'else'

# -*- special -*-
T_TYPE = 'type'
T_IDENTIFIER = 'identifier'
T_EOE = 'end_of_expression'
