from antlr4 import *
from joiParser import joiParser
from joiVisitor import joiVisitor

class VMCodeGenerator(joiVisitor):
    def __init__(self):
        self.instructions = [] 

    def visitProgram(self, ctx:joiParser.ProgramContext):
        self.visitChildren(ctx)
        return self.instructions
    
    def visitStatements(self, ctx:joiParser.StatementsContext):
        print("Hello <3")
        for statement in ctx.statement(): 
            self.visit(statement)  
            
    def visitStatement(self, ctx:joiParser.StatementContext):
        # print(ctx.getText())
        if ctx.printStmt():
            return self.visit(ctx.printStmt())
        elif ctx.inputStmt():
            return self.visit(ctx.inputStmt())
        elif ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        elif ctx.classFunctionAccessStmt():
            return self.visit(ctx.classFunctionAccessStmt())
        elif ctx.declarationStmt():
            return self.visit(ctx.declarationStmt())
        elif ctx.constDeclarationStmt():
            return self.visit(ctx.constDeclarationStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.switchStmt():
            return self.visit(ctx.switchStmt())
        elif ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        elif ctx.doWhileStmt():
            return self.visit(ctx.doWhileStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.deleteStmt():
            return self.visit(ctx.deleteStmt())
        elif ctx.tryCatchStmt():
            return self.visit(ctx.tryCatchStmt())
        elif ctx.throwStmt():
            return self.visit(ctx.throwStmt())
        
    def visitDeclarationStmt(self, ctx: joiParser.DeclarationStmtContext):
        if ctx.dataType() and ctx.varList():
            data_type = ctx.dataType().getText()  
            var_list = ctx.varList() 
           
            variables = self.visit(var_list)
           
            if ctx.expression():  
                self.visit(ctx.expression())  
                for var in variables:
                    self.instructions.append(f'DECLARE {data_type} {var}')  # Declaration
                    self.instructions.append(f'POP {var}')  # Store initialized value
            else:
                for var in variables:
                    self.instructions.append(f'DECLARE {data_type} {var}')  # Just declare if no assignment
        elif ctx.arrayDeclarationStmt():
            return self.visit(ctx.arrayDeclarationStmt())
        elif ctx.referenceDeclarationStmt():
            return self.visit(ctx.referenceDeclarationStmt())
        else:
            raise Exception("Unhandled declaration statement type")
        
    def visitVarList(self, ctx:joiParser.VarListContext):
        variables = []
        for var in ctx.IDENTIFIER():
            variables.append(var.getText())
        return variables

    def visitExpression(self, ctx:joiParser.ExpressionContext):
        if ctx.functionCall():
            return self.visit(ctx.functionCall())
        else:
            return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx:joiParser.LogicalOrExpressionContext):
        self.visit(ctx.logicalAndExpression(0))

        for i in range(1, len(ctx.logicalAndExpression())):
            self.visit(ctx.logicalAndExpression(i)) 
            self.instructions.append('OR') 
            
    def visitLogicalAndExpression(self, ctx:joiParser.LogicalAndExpressionContext):
        self.visit(ctx.rel_expr(0))

        for i in range(1, len(ctx.rel_expr())):
            self.visit(ctx.rel_expr(i))  
            self.instructions.append('AND') 

    def visitArithmeticOp(self, ctx:joiParser.ArithmeticOpContext):
        op = ctx.getText()
        if op == '+':
            self.instructions.append('ADD')
        elif op == '-':
            self.instructions.append('SUB')
        elif op == '*':
            self.instructions.append('MUL')
        elif op == '/':
            self.instructions.append('DIV')

    def visitAssignStmt(self, ctx: joiParser.AssignStmtContext):
        if ctx.IDENTIFIER() and ctx.expression(0) and not ctx.assignOp():
            var_name = ctx.IDENTIFIER().getText()  
            self.visit(ctx.expression(0))  
            self.instructions.append(f'POP {var_name}')  

        # (IDENTIFIER '[' expression ']' ('[' expression ']')* '=' expression ';')
        # should check this-------------------------------------
        elif ctx.IDENTIFIER() and ctx.expression(0) and ctx.expression(1):
            var_name = ctx.IDENTIFIER().getText()  
            index = self.visit(ctx.expression(0))  
            
            for i in range(1, len(ctx.expression()) - 1):
                index = self.visit(ctx.expression(i)) 

            self.instructions.append(f'PUSH_ARRAY {var_name}')  
            self.instructions.append(f'PUSH {index}')  
            self.visit(ctx.expression(-1))  
            self.instructions.append('POP_ARRAY') 

        # (IDENTIFIER assignOp expression ';')
        elif ctx.IDENTIFIER() and ctx.assignOp() and ctx.expression(0):
            var_name = ctx.IDENTIFIER().getText()  
            op = ctx.assignOp().getText()  
            
            self.instructions.append(f'PUSH {var_name}')  
            self.visit(ctx.expression(0))  
            
            if op == '+=':
                self.instructions.append('ADD')  
            elif op == '-=':
                self.instructions.append('SUB')  
            elif op == '*=':
                self.instructions.append('MUL')  
            elif op == '/=':
                self.instructions.append('DIV')  
            self.instructions.append(f'POP {var_name}')  

        # to be done
        elif ctx.structAssignStmt():
            return self.visit(ctx.structAssignStmt())  
        else:
            raise Exception("Unhandled assignment statement type")


    def visitReturnStmt(self, ctx:joiParser.ReturnStmtContext):
        if ctx.expression():
            self.visit(ctx.expression())
        self.instructions.append('RETURN')

    def visitRel_expr(self, ctx:joiParser.Rel_exprContext):
        # NOT rel_expr 
        if ctx.NOT():
            self.visit(ctx.rel_expr())  
            self.instructions.append('NOT')  
        else:
            self.visit(ctx.expr(0))
            
            for i in range(1, len(ctx.expr())):
                self.visit(ctx.expr(i))  
                comp_op = ctx.comparisonOp(i - 1).getText() 
                self.visitComparisonOp(comp_op) 
                
    def visitComparisonOp(self, op):
        if op == '==':
            self.instructions.append('EQ')  
        elif op == '!=':
            self.instructions.append('NEQ') 
        elif op == '>':
            self.instructions.append('GT')  
        elif op == '<':
            self.instructions.append('LT') 
        elif op == '>=':
            self.instructions.append('GTE') 
        elif op == '<=':
            self.instructions.append('LTE') 


    def visitExpr(self, ctx:joiParser.ExprContext):
        self.visit(ctx.term(0)) 
        
        for i in range(1, len(ctx.term())):
            self.visit(ctx.term(i))  
            op = ctx.getChild(2 * i - 1).getText()  
            
            if op == '+':
                self.instructions.append('ADD')  
            elif op == '-':
                self.instructions.append('SUB') 

    def visitTerm(self, ctx:joiParser.TermContext):
        self.visit(ctx.factor(0))  
        
        for i in range(1, len(ctx.factor())):
            self.visit(ctx.factor(i)) 
            op = ctx.getChild(2 * i - 1).getText()  
            if op == '*':
                self.instructions.append('MUL')
            elif op == '/':
                self.instructions.append('DIV')
            elif op == '%':
                self.instructions.append('MOD')

    def visitFactor(self, ctx:joiParser.FactorContext):
        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            
            if ctx.INC():  # pre-increment
                self.instructions.append(f'PUSH {var_name}')
                self.instructions.append('PUSH 1')
                self.instructions.append('ADD')
                self.instructions.append(f'POP {var_name}')
            elif ctx.DEC():  # pre-decrement
                self.instructions.append(f'PUSH {var_name}')
                self.instructions.append('PUSH 1')
                self.instructions.append('SUB')
                self.instructions.append(f'POP {var_name}')
                
            # Next 2 are not right-------------------------------------------
            elif ctx.getChildCount() > 1 and ctx.INC(1):  # post-increment 
                self.instructions.append(f'PUSH {var_name}')  
                self.instructions.append(f'PUSH {var_name}')
                self.instructions.append('PUSH 1')
                self.instructions.append('ADD')
                self.instructions.append(f'POP {var_name}')  
            elif ctx.getChildCount() > 1 and ctx.DEC(1):  # post-decrement 
                self.instructions.append(f'PUSH {var_name}')  
                self.instructions.append(f'PUSH {var_name}')
                self.instructions.append('PUSH 1')
                self.instructions.append('SUB')
                self.instructions.append(f'POP {var_name}')  
            
            elif ctx.expr():  
                for expr in ctx.expr():  
                    self.visit(expr)  
                self.instructions.append(f'PUSH_ARRAY {var_name}')  # should check this----------------
            else:
                self.instructions.append(f'PUSH {var_name}')  
        elif ctx.NUMBER():
            number = ctx.NUMBER().getText()
            self.instructions.append(f'PUSH {number}')  
        elif ctx.STRING():
            string_value = ctx.STRING().getText()
            self.instructions.append(f'PUSH "{string_value}"')  
        elif ctx.CHAR_LITERAL():
            char_value = ctx.CHAR_LITERAL().getText()
            self.instructions.append(f'PUSH {char_value}')  
        elif ctx.TRUE():
            self.instructions.append('PUSH 1')  
        elif ctx.FALSE():
            self.instructions.append('PUSH 0')  
        elif ctx.expr(): 
            self.visit(ctx.expr())  
        elif ctx.structAccessStmt():
            self.visit(ctx.structAccessStmt())  # to be done

    def visitMainFunction(self, ctx:joiParser.MainFunctionContext):
        self.instructions.append('LABEL MAIN')  
        self.visit(ctx.statements())  
        self.instructions.append('RETURN')  
        self.visit(ctx.expression())  
        self.instructions.append('HALT')  
