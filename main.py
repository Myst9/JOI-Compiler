from antlr4 import *
from joiLexer import joiLexer
from joiParser import joiParser
from vmCode_generator import VMCodeGenerator

def main():
    input_stream = FileStream('t.joi')
    lexer = joiLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = joiParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    # Initialize the VM code generator
    code_generator = VMCodeGenerator()
    code_generator.visit(tree)

    # Print generated VM instructions
    for instruction in code_generator.instructions:
        print(instruction)

if __name__ == "__main__":
    main()