from compiler.constants import (D_C_CURLYBRACKET, D_CBRACKET, D_COMMA,
                                D_O_CURLYBRACKET, D_OBRACKET, D_SEMICOLON,
                                LOG_AND, LOG_EQ, LOG_GE, LOG_GT, LOG_LE, LOG_LT, LOG_NEQ, LOG_OR,
                                OP_ASSIGNMENT, OP_CONCAT, OP_DIV, OP_MINUS, OP_MULTI,
                                OP_NOT, OP_PLUS, R_ELSE, R_IF, R_PRINTF, R_RETURN,
                                R_SCANF, R_WHILE, T_EOE, T_IDENTIFIER, T_INT, T_STR,
                                T_TYPE)
from compiler.errors import SyntaxError
from compiler.node import (Assignment, BinOp, Block, FuncCall, FuncDec, Identifier, If, IntVal,
                           NoOp, Printf, Return, Scanf, StrVal, UnOp, VarDec, While)
from compiler.tokenizer import Tokenizer


class Parser:
    tokens = None

    @staticmethod
    def parse_program():
        tokens = Parser.tokens
        declarations = [] # as statements
        while not tokens.current.type == T_EOE:
            declaration = Parser.parse_declaration()
            declarations.append(declaration)
        return Block(None, declarations)

    @staticmethod
    def parse_declaration():
        tokens = Parser.tokens

        declaration = FuncDec(None, [])

        if tokens.current.type != T_TYPE:
            raise SyntaxError(f"Expected '{T_TYPE}' and got {tokens.current}")

        vardec = VarDec(tokens.current.value, [])
        declaration.children.append(vardec)

        tokens.select_next()

        if tokens.current.type != T_IDENTIFIER:
            raise SyntaxError(
                f"Expected '{T_IDENTIFIER}' and got '{tokens.current}'")

        declaration.value = tokens.current.value  # function name
        vardec.children = [tokens.current.value]

        tokens.select_next()

        if tokens.current.type != D_OBRACKET:
            raise SyntaxError(f"Expected '{D_OBRACKET}' and got '{tokens.current}'")

        tokens.select_next()

        if tokens.current.type == T_TYPE:
            # variable declaration
            type = tokens.current.value
            
            tokens.select_next()
            
            if tokens.current.type != T_IDENTIFIER:
                raise SyntaxError(f"Expected '{T_IDENTIFIER}' and got '{tokens.current}'")
            
            arg_name = tokens.current.value
            declaration.children.append(VarDec(type, [arg_name]))

            tokens.select_next()
            
            while tokens.current.type == D_COMMA:
                tokens.select_next()

                if tokens.current.type != T_TYPE:
                    raise SyntaxError(f"Expected '{T_TYPE}' and got {tokens.current}")

                type = tokens.current.value
                
                tokens.select_next()

                if tokens.current.type != T_IDENTIFIER:
                    raise SyntaxError(f"Expected '{T_IDENTIFIER}' and got '{tokens.current}'")

                arg_name = tokens.current.value

                declaration.children.append(VarDec(type, [arg_name]))

                tokens.select_next()


        if tokens.current.type != D_CBRACKET:
            raise SyntaxError(f"Expected '{D_CBRACKET}' and got '{tokens.current}'")

        tokens.select_next()

        block = Parser.parse_block()
        declaration.children.append(block)

        return declaration

    @staticmethod
    def parse_block():

        tokens = Parser.tokens

        if tokens.current.type != D_O_CURLYBRACKET:
            raise SyntaxError(f"Block: expected '{D_O_CURLYBRACKET}' and got '{tokens.current}'")

        tokens.select_next()

        block = Block(None, [])

        while tokens.current.type != D_C_CURLYBRACKET:
            block.children.append(Parser.parse_statement())

        tokens.select_next()

        return block

    @staticmethod
    def parse_statement():
        tokens = Parser.tokens
        statement = NoOp(None)

        if tokens.current.type == D_SEMICOLON:
            tokens.select_next()

        elif tokens.current.type == T_IDENTIFIER:
            identifier = Identifier(tokens.current.value)
            tokens.select_next()

            if tokens.current.type != OP_ASSIGNMENT:
                raise SyntaxError(
                    f"Expected '{OP_ASSIGNMENT}' and got {tokens.current.type}")

            tokens.select_next()

            statement = Assignment(
                'assignment', [identifier, Parser.parse_rel_expression()])

            if tokens.current.type != D_SEMICOLON:
                raise SyntaxError(
                    f"Expected semicolon and got '{tokens.current}'")

            tokens.select_next()

        elif tokens.current.type == R_PRINTF:
            reserved = tokens.current
            tokens.select_next()

            if tokens.current.type != D_OBRACKET:
                raise SyntaxError(
                    f"Expected '{D_OBRACKET}' and got '{tokens.current.type}'")
            tokens.select_next()

            statement = Printf(reserved.value, [Parser.parse_rel_expression()])

            if tokens.current.type != D_CBRACKET:
                raise SyntaxError(
                    f"Expected '{D_CBRACKET}' and got '{tokens.current.type}'")

            tokens.select_next()

            if tokens.current.type != D_SEMICOLON:
                raise SyntaxError(f"Expected semicolon and got '{tokens.current}'")

            tokens.select_next()

        elif tokens.current.type == T_TYPE:
            statement = VarDec(tokens.current.value, [])
            tokens.select_next()

            if tokens.current.type != T_IDENTIFIER:
                raise SyntaxError(
                    f"Expected '{T_IDENTIFIER}' and got {tokens.current}")

            statement.children.append(tokens.current.value)
            tokens.select_next()

            while tokens.current.type == D_COMMA:
                tokens.select_next()

                if tokens.current.type != T_IDENTIFIER:
                    raise SyntaxError(
                        f"Expected '{T_IDENTIFIER}' and got {tokens.current}")

                statement.children.append((tokens.current.value))
                tokens.select_next()

            if tokens.current.type != D_SEMICOLON:
                raise SyntaxError(
                    f"Expected semicolon and got '{tokens.current}'")

            tokens.select_next()
        
        elif tokens.current.type == R_RETURN:
            tokens.select_next()

            if tokens.current.type != D_OBRACKET:
                raise SyntaxError(f"Expected '{D_OBRACKET}' and got '{tokens.current.type}'")

            tokens.select_next()

            statement = Return(R_RETURN, [Parser.parse_rel_expression()])

            if tokens.current.type != D_CBRACKET:
                raise SyntaxError(f"Expected '{D_CBRACKET}' and got '{tokens.current.type}'")

            tokens.select_next()

        elif tokens.current.type == R_WHILE:
            statement = While(tokens.current.value, [])
            tokens.select_next()

            if tokens.current.type != D_OBRACKET:
                raise SyntaxError(
                    f"Expected '{D_OBRACKET}' and got '{tokens.current.type}'")
            tokens.select_next()

            statement.children.append(Parser.parse_rel_expression())

            if tokens.current.type != D_CBRACKET:
                raise SyntaxError(f"Expected '{D_CBRACKET}' and got '{tokens.current.type}'")
            tokens.select_next()

            statement.children.append(Parser.parse_statement())

        elif tokens.current.type == R_IF:
            statement = If(tokens.current.value, [])
            tokens.select_next()

            if tokens.current.type != D_OBRACKET:
                raise SyntaxError(
                    f"Expected '{D_OBRACKET}' and got '{tokens.current.type}'")
            tokens.select_next()

            statement.children.append(Parser.parse_rel_expression())

            if tokens.current.type != D_CBRACKET:
                raise SyntaxError(
                    f"Expected '{D_CBRACKET}' and got '{tokens.current.type}'")
            tokens.select_next()

            statement.children.append(Parser.parse_statement())

            if tokens.current.type == R_ELSE:
                tokens.select_next()
                statement.children.append(Parser.parse_statement())

        else:
            statement = Parser.parse_block()

        return statement

    @staticmethod
    def parse_rel_expression():
        tokens = Parser.tokens

        N = Parser.parse_expression()

        while tokens.current.type in [LOG_EQ, LOG_NEQ, LOG_GT, LOG_GE, LOG_LT, LOG_LE]:
            op = tokens.current.type
            tokens.select_next()
            N = BinOp(op, [N, Parser.parse_expression()])

        return N

    @staticmethod
    def parse_expression():
        tokens = Parser.tokens

        N = Parser.parse_term()

        if tokens.current.type == T_INT:
            raise SyntaxError(f"Unexpected token: {tokens.current}")

        while tokens.current.type in [OP_PLUS, OP_MINUS, LOG_OR, OP_CONCAT]:

            if tokens.current.type == OP_PLUS:
                tokens.select_next()
                N = BinOp(OP_PLUS, [N, Parser.parse_term()])

            elif tokens.current.type == OP_MINUS:
                tokens.select_next()
                N = BinOp(OP_MINUS, [N, Parser.parse_term()])

            elif tokens.current.type == LOG_OR:
                tokens.select_next()
                N = BinOp(LOG_OR, [N, Parser.parse_term()])

            elif tokens.current.type == OP_CONCAT:
                tokens.select_next()
                N = BinOp(OP_CONCAT, [N, Parser.parse_expression()])

        return N

    @staticmethod
    def parse_term():
        tokens = Parser.tokens

        N = Parser.parse_factor()  # node

        while tokens.current.type in [OP_DIV, OP_MULTI, LOG_AND]:
            op = tokens.current.type
            tokens.select_next()
            N = BinOp(op, [N, Parser.parse_factor()])

        return N

    @staticmethod
    def parse_factor():
        tokens = Parser.tokens

        if tokens.current.type == T_INT:
            N = IntVal(tokens.current.value)
            tokens.select_next()

        elif tokens.current.type == T_STR:
            N = StrVal(tokens.current.value)
            tokens.select_next()

        elif tokens.current.type == T_IDENTIFIER:
            identifier_name = tokens.current.value
            tokens.select_next()

            if tokens.current.type == D_OBRACKET:
                tokens.select_next()
                
                N = FuncCall(identifier_name, [])

                if tokens.current.type != D_CBRACKET:
                    node = Parser.parse_rel_expression()
                    N.children.append(node)
                    while tokens.current.type == D_COMMA:
                        tokens.select_next()
                        node = Parser.parse_expression()
                        N.children.append(node)
                    tokens.select_next()
                else:
                    tokens.select_next()
            else:
                N = Identifier(identifier_name)

        elif tokens.current.type == OP_PLUS:
            tokens.select_next()
            N = UnOp(OP_PLUS, [Parser.parse_factor()])

        elif tokens.current.type == OP_MINUS:
            tokens.select_next()
            N = UnOp(OP_MINUS, [Parser.parse_factor()])

        elif tokens.current.type == OP_NOT:
            tokens.select_next()
            N = UnOp(OP_NOT, [Parser.parse_factor()])

        elif tokens.current.type == D_OBRACKET:
            tokens.select_next()

            N = Parser.parse_rel_expression()

            if tokens.current.type != D_CBRACKET:
                raise SyntaxError(f"Expected ')' and got {tokens.current}")

            tokens.select_next()

        elif tokens.current.type == R_SCANF:
            N = Scanf('scanf')

            tokens.select_next()

            if tokens.current.type != D_OBRACKET:
                raise SyntaxError(f"Expected '(' and got {tokens.current}")

            tokens.select_next()

            if tokens.current.type != D_CBRACKET:
                raise SyntaxError(f"Expected ')' and got {tokens.current}")

            tokens.select_next()

        else:
            raise SyntaxError(f"Unexpected token: {tokens.current}")

        return N

    @staticmethod
    def run(code):
        Parser.tokens = Tokenizer(code)
        Parser.tokens.select_next()

        program = Parser.parse_program()

        if Parser.tokens.current.type != T_EOE:
            raise SyntaxError(f"Unexpected token: {Parser.tokens.current}")

        program.children.append(FuncCall("main", []))

        return program
