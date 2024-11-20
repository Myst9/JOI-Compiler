from antlr4 import *
from joiLexer import joiLexer
from joiParser import joiParser
from vmCode_generator import VMCodeGenerator
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax Error at line {line}:{column} - {msg}")

def main():
    input_stream = FileStream('t.joi')
    lexer = joiLexer(input_stream)
    lexer.removeErrorListeners() 
    lexer.addErrorListener(MyErrorListener())  
    
    stream = CommonTokenStream(lexer)
    parser = joiParser(stream)
    parser.removeErrorListeners()  
    parser.addErrorListener(MyErrorListener())  
    
    try:
        tree = parser.program()
        # print(tree.toStringTree(recog=parser))
        
        # Initialize the VM code generator
        code_generator = VMCodeGenerator()
        code_generator.visit(tree)

        # Print generated VM instructions
        print("\nBEFORE OPTIMISATION JUST AFTER COMPILING")
        for instruction in code_generator.instructions:
            print(instruction)

        print("\nAFTER FUNCTION CALL OPTIMISATION\n")
        for instruction in code_generator.optimised_instructions:
            print(instruction)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
