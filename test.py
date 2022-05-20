from compiler import Lexer, Parser, load_file


def main():
    lexer = Lexer()
    parser = Parser()

    program = load_file("program.txt")
    tokens = lexer.tokenize(program)
    parser.parse(tokens)
    print(parser.back())


if __name__ == '__main__':
    main()
