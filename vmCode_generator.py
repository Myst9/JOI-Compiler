from antlr4 import *
from joiParser import joiParser
from joiVisitor import joiVisitor

ifqueue=[]
elseifqueue=[]
elsequeue=[]
whilequeue=[]
dowhilequeue=[]
switchqueue=[]
casequeue=[]
forqueue=[]
BreakOrContinueWhichLoop=[] #We will push which loop this statement belongs to when we enter the loop node so that when we encounter break statement
                    # we can direclty write JMP to end_{whatever} and when we come out of the loop node, we pop from it.
                    #If it is empty, it means it is not allowed and program breaks.
ifq=0
elseifq=0
elseq=0
whileq=0
dowhileq=0
switchq=0
caseq=0
forq=0

class VMCodeGenerator(joiVisitor):
    def __init__(self):
        self.instructions = [] 

    def visitProgram(self, ctx:joiParser.ProgramContext):
        self.visitChildren(ctx)
        return self.instructions
    
    def visitStatements(self, ctx:joiParser.StatementsContext):
        for statement in ctx.statement(): 
            self.visit(statement)  
            
    def visitStatement(self, ctx:joiParser.StatementContext):
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
            global ifq
            ifqueue.append(ifq)
            ifq+=1
            return self.visit(ctx.ifStmt())
        elif ctx.switchStmt():
            global switchq
            switchqueue.append(switchq)
            switchq+=1
            return self.visit(ctx.switchStmt())
        elif ctx.whileStmt():
            global whileq
            whilequeue.append(whileq)
            whileq+=1
            return self.visit(ctx.whileStmt())
        elif ctx.doWhileStmt():
            global dowhileq
            dowhilequeue.append(dowhileq)
            dowhileq+=1
            return self.visit(ctx.doWhileStmt())
        elif ctx.forStmt():
            global forq
            forqueue.append(forq)
            forq+=1
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
        
    def visitBreakStmt(self, ctx: joiParser.BreakStmtContext):
        if(BreakOrContinueWhichLoop):
            self.instructions.append(f'JMP, end_{BreakOrContinueWhichLoop[-1]}')
        else:
            pass # this is the case where break is not written in any loop but outside the loop.. we have to halt the 
                # code here. HOW DO WE DO THAT???

    def visitContinueStmt(self, ctx: joiParser.ContinueStmtContext):
        if(BreakOrContinueWhichLoop):
            self.instructions.append(f'JMP, {BreakOrContinueWhichLoop[-1]}')
        else:
            pass # this is the case where continue is not written in any loop but outside the loop.. we have to halt the 
                # code here. HOW DO WE DO THAT???
        
    def visitPrintStmt(self, ctx: joiParser.PrintStmtContext):
        to_be_printed_string=""
        for printexpression in ctx.printExpressionList():
            to_be_printed_string+=self.visit(printexpression)
        self.instructions.append(f'PRINT {printexpression}')
    
    def visitPrintExpressionList(self, ctx: joiParser.PrintExpressionListContext):
        if(ctx.expression()):
            ## return self.visit(ctx.expression())
            pass
            ## self.visit(ctx.expression()) returning noneType because answers are not returned..
            ## have to look into it once.. so for now Iam making it to pass
        return "\n"
        
    def visitDeclarationStmt(self, ctx: joiParser.DeclarationStmtContext):
        if ctx.dataType() and ctx.varList():
            data_type = ctx.dataType().getText()  
            var_list = ctx.varList() 
           
            variables = self.visit(var_list)
           
            if ctx.expression():  
                self.visit(ctx.expression())  
                for var in variables:
                    self.instructions.append(f'DECLARE {data_type} {var}')  # Declaration
                    self.instructions.append(f'STORE {var}') # Store initialized value
                    self.instructions.append(f'POP {var}') # since it is only declaration you can take it out.
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
            
            if ctx.INC():
                if(ctx.getChild(0).getText() == '++'):  # pre-increment
                    self.instructions.append(f'PUSH {var_name}')
                    self.instructions.append('PUSH 1')
                    self.instructions.append('ADD')
                    self.instructions.append(f'STORE {var_name}')
                else: #post-increment # the jugaad is to increase the value but not use it for operations. see below
                    self.instructions.append(f'PUSH {var_name}')
                    self.instructions.append('PUSH 1')
                    self.instructions.append('ADD')
                    self.instructions.append(f'STORE {var_name}') ##same like pre-incrment now var is var+1 and is stored
                    # now we subtract it by 1
                    self.instructions.append('PUSH 1')
                    self.instructions.append('SUB')
                    #now we have (var+1)-1 = var in the stack which can be used for the operations...
                    # so we increased var but did not use it instead we used the previous version for operations
                    # and stored the new version

            elif ctx.DEC():
                if(ctx.getChild(0).getText() == '--'):  # pre-decrement
                    self.instructions.append(f'PUSH {var_name}')
                    self.instructions.append('PUSH 1')
                    self.instructions.append('SUB')
                    self.instructions.append(f'STORE {var_name}')
                else: #post-decrement # the jugaad is to decrease the value but not use it for operations. see below
                    self.instructions.append(f'PUSH {var_name}')
                    self.instructions.append('PUSH 1')
                    self.instructions.append('SUB')
                    self.instructions.append(f'STORE {var_name}') ##same like pre-decrment now var is var-1 and is stored
                    # now we add 1 to it
                    self.instructions.append('PUSH 1')
                    self.instructions.append('ADD')
                    # now we have (var-1)+1 = var in the stack which can be used for the operations...
                    # so we decreased var but did not use it instead we used the previous version for operations
                    # and stored the new version

            ## this is how we can make post increment and decrement work without any problem.. 
            # as wanted old value is used for current operation and new value is already with us to use for next operation
            
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



    def visitAssignStmt(self, ctx: joiParser.AssignStmtContext):

        # if ctx.IDENTIFIER() and ctx.expression(0) and ctx.expression(1):
        if ctx.IDENTIFIER() and len(ctx.expression())>=2:
            var_name = ctx.IDENTIFIER().getText()  
            index = self.visit(ctx.expression(0))  
            
            for i in range(1, len(ctx.expression()) - 1):
                index = self.visit(ctx.expression(i)) 

            self.instructions.append(f'PUSH_ARRAY {var_name}')  
            self.instructions.append(f'PUSH {index}')  
            self.visit(ctx.expression(len(ctx.expression())-1))  
            self.instructions.append('POP_ARRAY') 
        elif ctx.IDENTIFIER() and ctx.expression(0) and not ctx.assignOp():
            var_name = ctx.IDENTIFIER().getText()  
            self.visit(ctx.expression(0))  
            self.instructions.append(f'STORE {var_name}')  
            self.instructions.append(f'POP {var_name}')  

        # (IDENTIFIER '[' expression ']' ('[' expression ']')* '=' expression ';')
        # should check this-------------------------------------


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
            
            self.instructions.append(f'STORE {var_name}')
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

    def visitIfStmt(self, ctx: joiParser.IfStmtContext):
        self.visit(ctx.condition())
        global elseifqueue, elseifq, elseq, elseifqueue, ifq, elsequeue
        k=0
        if(len(ctx.elseIfStmt())>0):
            k=1
            for i in range(elseifq+len(ctx.elseIfStmt())-1, elseifq-1, -1):
                elseifqueue.append(i)
            elseifq+=len(ctx.elseIfStmt())
        if(ctx.elseStmt()):
            k=1
            elsequeue.append(elseq)
            elseq+=1

        if(k):
            if(len(elseifqueue)>0):
                self.instructions.append(f'JZ, elseif_{elseifqueue[-1]}')
            elif(elsequeue):
                self.instructions.append(f'JZ, else_{elsequeue[-1]}')
        else:
            self.instructions.append(f'JZ, end_if_{ifqueue[-1]}')

        self.visit(ctx.statements())
        self.instructions.append(f'JMP, end_if_{ifqueue[-1]}')

        for elseifstmt in ctx.elseIfStmt():
            self.instructions.append(f'elseif_{elseifqueue[-1]}:')
            elseifqueue.pop()
            self.visit(elseifstmt)
            self.instructions.append(f'JMP, end_if_{ifqueue[-1]}')

        if(ctx.elseStmt()):
            self.instructions.append(f'else_{elsequeue[-1]}:')
            self.visit(ctx.elseStmt())
            elsequeue.pop()
        self.instructions.append(f'end_if_{ifqueue[-1]}:')
        ifqueue.pop()

    def visitElseIfStmt(self, ctx: joiParser.ElseIfStmtContext):
        self.visit(ctx.condition())
        global elseifqueue, elseifq, elseq, elseifqueue, ifq, elsequeue
        if(elseifqueue):
            self.instructions.append(f'JZ, elseif_{elseifqueue[-1]}')
        else:
            self.instructions.append(f'JZ, else_{elsequeue[-1]}')
        self.visit(ctx.statements())

    def visitElseStmt(self, ctx: joiParser.ElseStmtContext):
        self.visit(ctx.statements())

    def visitWhileStmt(self, ctx: joiParser.WhileStmtContext):
        global whilequeue, whileq, BreakOrContinueWhichLoop
        BreakOrContinueWhichLoop.append(f'while_{whilequeue[-1]}')
        self.instructions.append(f'while_{whilequeue[-1]}:')
        self.visit(ctx.condition())
        self.instructions.append(f'JZ, end_while_{whilequeue[-1]}')
        self.visit(ctx.statements())
        self.instructions.append(f'JMP, while_{whilequeue[-1]}')
        self.instructions.append(f'end_while_{whilequeue[-1]}:')
        whilequeue.pop()
        BreakOrContinueWhichLoop.pop()

    def visitDoWhileStmt(self, ctx: joiParser.DoWhileStmtContext):
        global dowhilequeue, dowhileq, BreakOrContinueWhichLoop
        BreakOrContinueWhichLoop.append(f'do_while_{dowhilequeue[-1]}')
        self.instructions.append(f'do_while_{dowhilequeue[-1]}:')
        self.visit(ctx.statements())
        self.visit(ctx.condition())
        self.instructions.append(f'JZ, end_do_while_{dowhilequeue[-1]}')
        self.instructions.append(f'JMP, do_while_{dowhilequeue[-1]}')
        self.instructions.append(f'end_do_while_{dowhilequeue[-1]}:')
        dowhilequeue.pop()
        BreakOrContinueWhichLoop.pop()

    def visitSwitchStmt(self, ctx: joiParser.SwitchStmtContext):
        global switchq, switchqueue, caseq, casequeue
        self.visit(ctx.expression())
        for i in range(caseq+len(ctx.caseStmt())-1, caseq-1, -1):
            casequeue.append(i)
        caseq+=len(ctx.caseStmt())

        for case in ctx.caseStmt():
            self.instructions.append(f'case_{casequeue[-1]}:')
            casequeue.pop()
            self.visit(case)

        self.instructions.append(f'default_{switchqueue[-1]}:')
        if(ctx.defaultStmt()):
            self.visit(ctx.defaultStmt())
        self.instructions.append(f'end_switch_{switchqueue[-1]}:')
        switchqueue.pop()
            
    def visitCaseStmt(self, ctx: joiParser.CaseStmtContext):
        global casequeue, switchqueue
        self.visit(ctx.expression())
        if(casequeue):
            self.instructions.append(f'JZ, case_{casequeue[-1]}')
        else:
            self.instructions.append(f'JZ, default_{switchqueue[-1]}')
        self.visit(ctx.statements())
        self.instructions.append(f'JMP, end_switch_{switchqueue[-1]}')

    def visitDefaultStmt(self, ctx: joiParser.DefaultStmtContext):
        self.visit(ctx.statements())

    def visitForStmt(self, ctx: joiParser.ForStmtContext):
        global forq, forqueue, BreakOrContinueWhichLoop
        BreakOrContinueWhichLoop.append(f'for_{forqueue[-1]}')
        self.visit(ctx.forInit())
        self.instructions.append(f'for_{forqueue[-1]}:')
        if(ctx.condition()):
            self.visit(ctx.condition())
            self.instructions.append(f'JZ, end_for_{forqueue[-1]}')
        self.visit(ctx.statements())
        self.visit(ctx.forUpdate())
        self.instructions.append(f'JMP, for_{forqueue[-1]}')
        self.instructions.append(f'end_for_{forqueue[-1]}:')
        forqueue.pop()
        BreakOrContinueWhichLoop.pop()

    def visitForInit(self, ctx: joiParser.ForInitContext):
        if(ctx.assignStmt()):
            self.visit(ctx.assignStmt())
        elif(ctx.declarationStmt()):
            for declaration in ctx.declarationStmt():
                self.visit(declaration)

    def visitForUpdate(self, ctx: joiParser.ForUpdateContext):
        self.visit(ctx.expression())







    def visitCondition(self, ctx: joiParser.ConditionContext):
        self.visit(ctx.expression())

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








    def visitMainFunction(self, ctx:joiParser.MainFunctionContext):
        self.instructions.append('LABEL MAIN')  
        self.visit(ctx.statements())  
        self.instructions.append('RETURN')  
        self.visit(ctx.expression())  
        self.instructions.append('HALT')  
