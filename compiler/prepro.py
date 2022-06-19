from compiler.errors import SyntaxError

import re


class PrePro:
    @staticmethod
    def remove_hash_comment(expression):
        regxp = re.compile('#.+\n?')
        return re.sub(regxp, '', expression)

    @staticmethod
    def remove_block_comment(expression):
        start = expression.find('/*')
        end = expression.find('*/')

        if start == -1 and end == -1:
            return expression

        if end == -1:
            raise SyntaxError("Comment block doesn't close")

        replace_string = expression[start:end + 2]
        expression = expression.replace(replace_string, '', 1)

        return PrePro.remove_block_comment(expression)

    @staticmethod
    def filter(expression):
        expression = PrePro.remove_hash_comment(expression)
        expression = PrePro.remove_block_comment(expression)
        return expression
