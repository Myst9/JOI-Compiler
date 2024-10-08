from antlr4 import *
from joiLexer import joiLexer
from joiParser import joiParser
from tac_generator import TACGenerator

def main():
    input_stream = FileStream('test3.joi')
    lexer = joiLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = joiParser(stream)
    tree = parser.program()
    # print(tree.toStringTree(recog=parser))

    # tac_generator = TACGenerator()
    # tac_generator.visit(tree)

    # print("Three Address Code:")
    # print(tac_generator.getTAC())

if __name__ == "__main__":
    main()
