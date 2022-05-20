# -*- encoding :: utf-8 -*-

from sly import Parser as SlyParser
from .lexer import Lexer

from .utils import Stack, load_file


class Parser(SlyParser):
    # código baseado na documentação do SLY
    # https://sly.readthedocs.io/en/latest/sly.html#writing-a-parser
    tokens = Lexer.tokens
    
    def back(self):
        return self.stack.back

    # @_('')
    # def statement(self, p):
    #     pass

    # @_('operation')
    # def expression(self, p):
    #     pass

    # @_('literal')  # This must be added to avoid infinite recursion
    # def expression(self, p):
    #     pass

    @_('')
    def empty(self, p):
        pass

    @_('statement')
    def top_level(self, p):
        return p.value

    @_('T_OPENING_CURLY_BRACKET statement T_CLOSING_CURLY_BRACKET')
    def block(self, p):
        return p.value

    @_('TYPE IDENTIFIER', 'TYPE IDENTIFIER')
    def identifier_declaration(self, p):
        type = p[0]
        return (type, p.IDENTIFIER)

    @_('TYPE IDENTIFIER T_OPENING_BRACKET empty T_CLOSING_BRACKET BLOCK')
    def function_declaration(self, p):
        return (p.TYPE, p.IDENTIFIER, p.BLOCK)

    @_('TYPE IDENTIFIER')

    @_('term T_PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('term T_MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term LOG_OR term')
    def expr(self, p):
        return p.expr or p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('factor T_MULTI factor')
    def term(self, p):
        return p.term * p.factor

    @_('factor T_DIV factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor LOG_AND factor')
    def term(self, p):
        return p.term and p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @_('IDENTIFIER')
    def factor(self, p):
        return p.IDENTIFIER

    @_('function_call')
    def factor(self, p):
        return p

    @_(r'')
    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

    # @_('')
    # def expression(self, p):
    #     pass

    @_('NUMBER T_PLUS NUMBER')
    def operation(self, p):
        self.stack.push(p.NUMBER0 + p.NUMBER1)

    @_('NUMBER T_MINUS NUMBER')
    def operation(self, p):
        self.stack.push(p.NUMBER0 - p.NUMBER1)

    @_('NUMBER T_MULTI NUMBER')
    def operation(self, p):
        self.stack.push(p.NUMBER0 * p.NUMBER1)

    @_('NUMBER T_DIV NUMBER')
    def operation(self, p):
        self.stack.push(p.NUMBER0 // p.NUMBER1)

    @_('IDENTIFIER T_ASSIGNMENT expression')
    def operation(self, p):
        self.stack.push()
    """
    # @_("TOP_LEVEL")
    @_('STATEMENT')
    def operation(self, p):
        pass

    # @_("BLOCK")
    @_('T_OPENING_CURLY_BRACKET STATEMENT T_CLOSING_CURLY_BRACKET ')
    def operation(self, p):
        pass

    # @_("TYPE")
    @_('"integer" | "string" ')
    def operation(self, p):
        pass

    # @_("IDENTIFIER_DECLARATION")
    @_('TYPE , IDENTIFIER ')
    def operation(self, p):
        pass

    # @_("FUNCTION_DEFINITION")
    @_('TYPE , IDENTIFIER , "(" [ , TYPE, IDENTIFIER [ , { "," , TYPE, IDENTIFIER } ] ] , ")" , BLOCK ')
    def operation(self, p):
        pass

    # @_("FUNCTION_CALL")
    @_('IDENTIFIER , "(" [ , IDENTIFIER [ , { "," , IDENTIFIER } ] ] , ")" ')
    def operation(self, p):
        pass

    # @_("STATEMENT")
    @_('( λ | IDENTIFIER_DECLARATION | FUNCTION_DEFINITION | FUNCTION_CALL | ASSIGNMENT | BLOCK | WHILE_STATEMENT | IF_STATEMENT ), ";" ')
    def operation(self, p):
        pass

    # @_("FACTOR")
    @_('( NUMBER | IDENTIFIER | FUNCTION_CALL | ( UNNARY_OPERATOR , FACTOR ) | "(" , CONDITIONAL , ")" )')
    def operation(self, p):
        pass

    # @_("TERM")
    @_('FACTOR, { ("\*" | "/" | "and"), FACTOR } ')
    def operation(self, p):
        pass

    # @_("EXPRESSION")
    @_('TERM, { ("+" | "-" | "or"), TERM } ')
    def operation(self, p):
        pass

    # @_("CONDITIONAL")
    @_('EXPRESSION , { ("<" | "<=" | "==" | "!=" | ">=" | ">" ) , EXPRESSION } ')
    def operation(self, p):
        pass

    # @_("WHILE_STATEMENT")
    @_('"while" , "(" , CONDITIONAL , ")" , BLOCK ')
    def operation(self, p):
        pass

    # @_("IF_STATEMENT")
    @_('"if" , "(" , CONDITIONAL , ")" , BLOCK , [ "else" , BLOCK ] ')
    def operation(self, p):
        pass

    # @_("ASSIGNMENT")
    @_('IDENTIFIER, "=" , EXPRESSION ')
    def operation(self, p):
        pass
   """


if __name__ == "__main__":
    parser = Parser()
    text = load_file('program.txt')
    # tokens = parser.(text)
    # for token in tokens:
    # print(token)
