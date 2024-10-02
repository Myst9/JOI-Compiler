from joiParser import joiParser
from joiVisitor import joiVisitor
from antlr4 import *

class TACGenerator(joiVisitor):
    def __init__(self):
        self.temp_counter = 0  # To keep track of temporary variables
        self.tac = []  # List to store TAC instructions
        self.label_counter = 0  # To create unique labels

    def next_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def next_label(self):
        self.label_counter += 1
        return f"L{self.label_counter}"

    # Handle #include <iostream>
    def visitIncludeStmt(self, ctx: joiParser.IncludeStmtContext):
        self.tac.append("#include <iostream>")
        return None

    # Visit the print statement node
    def visitPrintStmt(self, ctx: joiParser.PrintStmtContext):
        expressions = ctx.printExpressionList().expression()
        temp_vars = []

        # Process each expression
        for expr in expressions:
            temp = self.visit(expr)
            temp_vars.append(temp)

        # If multiple expressions, concatenate them
        if temp_vars:
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
            return ctx.STRING().getText().strip('"')
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.getChildCount() == 3:  # Binary operation
            left = self.visit(ctx.expression(0))
            op = ctx.getChild(1).getText()  # Get operator
            right = self.visit(ctx.expression(1))
            temp = self.next_temp()
            self.tac.append(f"{temp} = {left} {op} {right}")
            return temp
        elif ctx.getChildCount() == 1:  # Single operand
            return self.visit(ctx.getChild(0))
        return None

    # Visit if statements
    def visitIfStmt(self, ctx: joiParser.IfStmtContext):
        condition = self.visit(ctx.condition())
        true_label = self.next_label()
        false_label = self.next_label()

        self.tac.append(f"if {condition} goto {true_label}")
        self.tac.append(f"goto {false_label}")
        self.tac.append(f"{true_label}:")
        for statement in ctx.statements():
            self.visit(statement)
        self.tac.append(f"{false_label}:")

        
        # Handle else statement
        if ctx.ELSE():
            self.tac.append(f"{false_label}:")
            for statement in ctx.statements():
                self.visit(statement)
        return None

    # Visit while statements
    def visitWhileStmt(self, ctx: joiParser.WhileStmtContext):
        start_label = self.next_label()
        end_label = self.next_label()

        self.tac.append(f"{start_label}:")
        condition = self.visit(ctx.condition())
        self.tac.append(f"if {condition} goto {end_label}")
        for statement in ctx.statements():
            self.visit(statement)
        self.tac.append(f"goto {start_label}")
        self.tac.append(f"{end_label}:")
        return None

    # Visit for statements
    def visitForStmt(self, ctx: joiParser.ForStmtContext):
        # Handle initialization, condition, increment, and body
        init = self.visit(ctx.forInit())
        condition = self.visit(ctx.condition())
        increment = self.visit(ctx.forUpdate())

        start_label = self.next_label()
        end_label = self.next_label()

        self.tac.append(f"{init}")  # Initialization statement
        self.tac.append(f"{start_label}:")
        self.tac.append(f"if {condition} goto {end_label}")
        for statement in ctx.statements():
            self.visit(statement)
        self.tac.append(increment)  # Increment statement
        self.tac.append(f"goto {start_label}")
        self.tac.append(f"{end_label}:")
        return None

    # Visit return statement
    def visitReturnStmt(self, ctx: joiParser.ReturnStmtContext):
        ret_value = self.visit(ctx.expression())
        self.tac.append(f"return {ret_value}")
        return None

    # Visit the main function
    def visitMainFunction(self, ctx: joiParser.MainFunctionContext):
        self.visitChildren(ctx)
        return None

    # Get the TAC output as a string
    def getTAC(self):
        return "\n".join(self.tac)
