from sly import Lexer as SlyLexer

from compiler.utils import load_file


class Lexer(SlyLexer):
    # Lexer baseado em um artigo do Medium:
    # https://yahel-oppenheimer.medium.com/create-your-own-scripting-language-in-python-with-sly-7b864e762e07

    tokens = {
        NUMBER,
        # operations
        T_PLUS, T_MINUS, T_MULTI, T_DIV, T_ASSIGNMENT,
        # logical operations
        LOG_OR, LOG_AND, LOG_EQ, LOG_NEQ, LOG_GE, LOG_GT, LOG_LE, LOG_LT, LOG_NOT,
        # delimiters
        T_OPENING_CURLY_BRACKET, T_CLOSING_CURLY_BRACKET, T_OPENING_BRACKET, T_CLOSING_BRACKET, STRING,
        # types
        IF, ELSE, WHILE, TYPE,

        IDENTIFIER, T_COMMENT
    }

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

    ignore = ' \t\n'

    literals = {'.', ';', ','}

    @_(r"(0|[1-9][0-9]*)")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')
    def STRING(self, t):
        t.value = self.remove_quotes(t.value)
        return t

    TYPE = r'integer|string'
    IF = r'if'
    ELSE = r'else'
    WHILE = r'while'

    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'

    def remove_quotes(self, text: str):
        if text.startswith('\"'):
            return text[1:-1]
        return text


if __name__ == "__main__":
    lexer = Lexer()
    text = load_file('program.txt')
    tokens = lexer.tokenize(text)
    for token in tokens:
        print(token)
