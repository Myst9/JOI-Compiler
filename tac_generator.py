from joiParser import joiParser
from joiVisitor import joiVisitor
from joiLexer import joiLexer
from antlr4 import *

class TACGenerator(joiVisitor):

    def __init__(self):
        self.temp_counter = 0  # To keep track of temporary variables
        self.tac = []  # List to store TAC instructions

    def next_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    # Visit the print statement node
    def visitPrintStmt(self, ctx: joiParser.PrintStmtContext):
        expressions = ctx.printExpressionList().expression()
        temp_vars = []

        # Process each expression
        for expr in expressions:
            temp = self.visit(expr)
            temp_vars.append(temp)

        # If multiple expressions, concatenate them
        result = temp_vars[0]
        for expr in temp_vars[1:]:
            next_temp = self.next_temp()
            self.tac.append(f"{next_temp} = {result} + {expr}")
            result = next_temp

        self.tac.append(f"print {result}")
        return None

    # Visit the input statement node
    def visitInputStmt(self, ctx: joiParser.InputStmtContext):
        variable = ctx.IDENTIFIER().getText()
        self.tac.append(f"input {variable}")
        return None

    # Visit the assignment statement node
    def visitAssignStmt(self, ctx: joiParser.AssignStmtContext):
        variable = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        self.tac.append(f"{variable} = {value}")
        return None

    # Visit expression nodes
    def visitExpression(self, ctx: joiParser.ExpressionContext):
        if ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()

    # Visit return statement
    def visitMainFunction(self, ctx: joiParser.MainFunctionContext):
        self.visitChildren(ctx)
        ret_value = ctx.NUMBER().getText()
        self.tac.append(f"return {ret_value}")

    # Get the TAC output as a string
    def getTAC(self):
        return "\n".join(self.tac)
