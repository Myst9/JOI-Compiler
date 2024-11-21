from antlr4 import *
from joiLexer import joiLexer
from joiParser import joiParser
from vmCode_generator import VMCodeGenerator
from antlr4.error.ErrorListener import ErrorListener
import os

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax Error at line {line}:{column} - {msg}")

def main():
    # input_folder = "C:\Users\User\Desktop\JOI Compiler\joi"
    # output_folder = os.path.join(input_folder, "output")
    input_folder = "./joi"
    output_folder = os.path.join(input_folder, "output")
    os.makedirs(output_folder, exist_ok=True)
    
    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".joi"):
            # Read the content of the .joi file
            input_path = os.path.join(input_folder, filename)
           
            input_stream = FileStream(input_path)
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
                # print("\nBEFORE OPTIMISATION JUST AFTER COMPILING")
                # for instruction in code_generator.instructions:
                #     print(instruction)

                # print("\nAFTER FUNCTION CALL OPTIMISATION\n")
                # for instruction in code_generator.optimised_instructions:
                #     print(instruction)

            except Exception as e:
                print(e)
            
            # Define the output .vm file path
            output_filename = f"{os.path.splitext(filename)[0]}.vm"
            output_path = os.path.join(output_folder, output_filename)
            
            # Write the processed content to the .vm file (modify if needed)
            with open(output_path, 'w') as vm_file:
                # Placeholder processing logic - just copying content for now
                printingstmt=""
                for instruction in code_generator.optimised_instructions:
                    printingstmt+=instruction+"\n"
                vm_file.write(printingstmt)
            
            print(f"Processed: {filename} -> {output_filename}")
    

if __name__ == "__main__":
    main()
