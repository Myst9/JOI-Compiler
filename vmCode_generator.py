from antlr4 import *
from joiParser import joiParser
from joiVisitor import joiVisitor
import sys
from symbolTable import SymbolTable

#ytd means yet to be decided
# you'll see in some parts of code

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

symbolTable = SymbolTable()

def ExitFromProgram(errormessage):
    print(errormessage)
    sys.exit()

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
        elif ctx.objectDeclarationStmt():
            return self.visit(ctx.objectDeclarationStmt())
        elif ctx.structDeclarationStmt():
            return self.visit(ctx.structDeclarationStmt())
        

    def visitStructDeclarationStmt(self, ctx: joiParser.StructDeclarationStmtContext):
        struct_class = ctx.IDENTIFIER(0).getText()
        struct_name= ctx.IDENTIFIER(1).getText()



    def visitInputStmt(self, ctx: joiParser.InputStmtContext):
        var_info = self.visit(ctx.idOrPointerOrAddrId())
        var_name = var_info[1]
        var_type = var_info[0]
        if(not symbolTable.read(var_name)):
            ExitFromProgram(f'cannot take input for undeclared variable {var_name}')
        if(var_type=='address_identifier'):
            ExitFromProgram(f'cannot take input into a referenced variable {var_name}')
        self.instructions.append(f'INPUT {var_name}')
    
    def visitDeleteStmt(self, ctx: joiParser.DeleteStmtContext):
        var_info = self.visit(ctx.idOrPointerOrAddrId())
        var_name = var_info[1]
        var_type = var_info[0]
        if(not symbolTable.read(var_name)):
            ExitFromProgram(f'cannot delete undeclared variable {var_name}')
        if((symbolTable.read(var_name))['type']!='pointer'):
            ExitFromProgram(f'please provide a pointer to delete')
        symbolTable.delete(var_name)
        self.instructions.append(f'DELETE {var_name}')#I exactly dont know, just put it here as of now
        
    def visitReferenceDeclarationStmt(self, ctx: joiParser.ReferenceDeclarationStmtContext):
        data_type = ctx.dataType().getText()
        
        var_name = self.visit(ctx.address_identifier())[1]
        if(symbolTable.read(var_name)):
            ExitFromProgram(f'already declared {var_name}. cannot reference declare it.')
        referenced_info = self.visit(ctx.idOrPointerOrAddrId())#[type, name]
        referenced_name = referenced_info[1]
        referenced_type = referenced_info[0] #pointer or address or variable
        if(referenced_type=='address_identifier'):
            ExitFromProgram(f'cannot bind {referenced_name} to {var_name}')

        symbolTable.create(name=var_name, symbol_type='reference',scope='ytd',datatype=data_type)
        for expr in ctx.expression():
            self.visit(expr)

    
    def visitObjectDeclarationStmt(self, ctx: joiParser.ObjectDeclarationStmtContext):
        class_name = ctx.IDENTIFIER(0).getText()
        object_name = ctx.IDENTIFIER(1).getText()
        constructor_name = ctx.IDENTIFIER(2).getText()
        # if(symbolTable.read(object_name)):
        #     ExitFromProgram(f'already declared {object_name}. use another name.')
        # if(not symbolTable.read(class_name) or not symbolTable.read(constructor_name)):
        #     ExitFromProgram(f'{class_name} or {constructor_name} is not declared yet. Please check')
        # if((symbolTable.read(class_name))['type']!='class' or (symbolTable.read(constructor_name))['type']!='class'):
        #     ExitFromProgram(f'{class_name} or {constructor_name} is not a class. cannot make a object')
        symbolTable.create(name=object_name, symbol_type='object',scope='ytd', datatype=class_name)
        self.instructions.append(f'DECLARE {class_name} {object_name}')
        if(ctx.expression()):
            self.instructions.append(f'ARG_for_CNSTRCTR') # still need to write upward push for expression results
            for expr in ctx.expression():
                self.visit(expr)
            self.instructions.append(f'ARGS END')
        
        
        
        
        
    def visitConstDeclarationStmt(self, ctx: joiParser.ConstDeclarationStmtContext):
        variables = self.visit(ctx.declarationStmt())
        for var in variables:
            symbolTable.update(name=var, symbol_type='constant')
        
    def visitBreakStmt(self, ctx: joiParser.BreakStmtContext):
        if(BreakOrContinueWhichLoop):
            self.instructions.append(f'JMP, end_{BreakOrContinueWhichLoop[-1]}')
        else:
            ExitFromProgram("break written outside loop")
            pass # this is the case where break is not written in any loop but outside the loop.. we have to halt the 
                # code here. HOW DO WE DO THAT???

    def visitContinueStmt(self, ctx: joiParser.ContinueStmtContext):
        if(BreakOrContinueWhichLoop):
            self.instructions.append(f'JMP, {BreakOrContinueWhichLoop[-1]}')
        else:
            ExitFromProgram("continue written outside loop")
            pass # this is the case where continue is not written in any loop but outside the loop.. we have to halt the 
                # code here. HOW DO WE DO THAT???
        
    def visitPrintStmt(self, ctx: joiParser.PrintStmtContext):
        to_be_printed_string=""
        for printexpression in ctx.printExpressionList():
            to_be_printed_string+=self.visit(printexpression)
        self.instructions.append(f'PRINT {printexpression}')
    
    def visitPrintExpressionList(self, ctx: joiParser.PrintExpressionListContext):
        if(ctx.expression()):
            # return self.visit(ctx.expression())
            pass
            ## self.visit(ctx.expression()) returning noneType because answers are not returned..
            ## have to look into it once.. so for now Iam making it to pass
        return "\n"
    
    def visitFunctionDef(self, ctx: joiParser.FunctionDefContext):
        return_type="void"
        if(ctx.dataType()):
            return_type = ctx.dataType().getText() 
        func_name = ctx.IDENTIFIER().getText()
        if(symbolTable.read(func_name)):
            ExitFromProgram("The name already exists. Use a different name.")
        self.instructions.append(f'FUNC_{func_name}:')
        symbolTable.create(name=func_name, symbol_type='function', scope='ytd', returntype=return_type)
        
        
        if(ctx.paramList()):
            params = self.visitParamList(ctx.paramList()) 
            for param in params:
                self.instructions.append(f'param {param}')
        self.visit(ctx.statements())
        if(ctx.returnStmt()):
            self.visit(ctx.returnStmt())

    def visitParamList(self, ctx: joiParser.ParamListContext):
        params = []
        for param in ctx.param():
            params.append(self.visit(param))
        return params
    
    def visitParam(self, ctx: joiParser.ParamContext):#need to add scope when adding to symbol table
        if(ctx.dataType()):
            data_type = ctx.dataType().getText()
        param_info = [None, None]

        param_info = self.visit(ctx.idOrPointerOrAddrId())
        param_name = param_info[1]
        param_type = param_info[0]

        if(symbolTable.read(param_name)):# need to implement scope for this.. as of now only name checking is done
            ExitFromProgram("param name is already used in the code. Try different name.")
        symbolTable.create(name=param_name, symbol_type='parameter', scope='ytd',datatype=data_type, paramtype=param_type)
        return param_name
    
    def visitFunctionCall(self, ctx: joiParser.FunctionCallContext):
        if(ctx.argList()):
            self.instructions.append(f'ARGS_START')
            arguments = self.visit(ctx.argList())
            self.instructions.append(f'ARGS END')
        
        if(len(ctx.IDENTIFIER())==1):
            func_name = ctx.IDENTIFIER(len(ctx.IDENTIFIER())-1).getText()
            if(not symbolTable.read(func_name)):
                ExitFromProgram("No such function to call")
            
            # if(arguments):
            #     for arg in arguments: # this can be written once expression starts returning things... TejA work on that 
            #         self.instructions.append(f'ARGS {arg}')
            self.instructions.append(f'CALL {func_name}')

    
    def visitArgList(self, ctx: joiParser.ArgListContext):
        arguments = []
        for argum in ctx.expression():
            arguments.append(self.visit(argum))
        return arguments


    def visitReferenceDataType(self, ctx: joiParser.ReferenceDataTypeContext):
        return ctx.getChild(0).getText()

    def visitDeclarationStmt(self, ctx: joiParser.DeclarationStmtContext):
        
        if ctx.dataType() and ctx.varList():
            data_type = ctx.dataType(0).getText()  
            var_list = ctx.varList() 
            variables = self.visit(var_list)
           
            if not ctx.NEW() and ctx.expression():  
                self.visit(ctx.expression())  
                for var in variables:
                    if(symbolTable.read(var[1])):# if the variable is already declared somewhere.. doesn't matter if it is var or func or array. once declared cannot be used again
                        ExitFromProgram(f'already declared {var[1]} variable')
                    self.instructions.append(f'DECLARE {data_type} {var[1]}')  # Declaration
                    self.instructions.append(f'STORE {var[1]}') # Store initialized value
                    symbolTable.create(name=var[1], symbol_type=var[0], scope='ytd', datatype=data_type, value='ytd') # we don't know how to get expression value to put it here
                    self.instructions.append(f'POP {var[1]}') # since it is only declaration you can take it out.
            else:
                # print(variables)
                # for expr in ctx.expression():
                #     self.visit(expr)
                for var in variables:
                    if(symbolTable.read(var[1])):# if the variable is already declared somewhere.. doesn't matter if it is var or func or array. once declared cannot be used again
                        ExitFromProgram(f'already declared {var[1]} variable')
                    self.instructions.append(f'DECLARE {data_type} {var[1]}')  # Just declare if no assignment
                    symbolTable.create(name=var[1], symbol_type='pointer', scope='ytd', datatype=data_type)

            return variables
        elif(ctx.arrayDeclarationStmt()):
            return self.visit(ctx.arrayDeclarationStmt())
        else:
            raise Exception("Unhandled declaration statement type")
    
    def visitArrayDeclarationStmt(self, ctx: joiParser.ArrayDeclarationStmtContext):
        
        data_type = ctx.dataType().getText()  
        arrayinfo = self.visit(ctx.idOrPointerOrAddrId())
        arrayName = arrayinfo[1] 
        if(symbolTable.read(arrayName)):# if the variable is already declared somewhere.. doesn't matter if it is var or func or array. once declared cannot be used again
            ExitFromProgram(f'already declared {arrayName} variable')
        if(arrayinfo[0]=='address_identifier'):
            ExitFromProgram(f'cannot create {arrayName} array of references')
        symbolTable.create(name=arrayName, symbol_type='array', scope='ytd', datatype=data_type)
        for expression in ctx.expression():
            self.visit(expression)
        
        if(ctx.arrayValueAssigning()):
            self.visit(ctx.arrayValueAssigning())
        


    def visitArrayValueAssigning(self, ctx: joiParser.ArrayValueAssigningContext):
        for assigning in ctx.arrayValueAssigning():
            self.visit(assigning)
        if(ctx.expression()):
            self.visit(ctx.expression())

    def visitVarList(self, ctx:joiParser.VarListContext):
        variables = []
        for var in ctx.var():
            variables.append(self.visit(var))
        return variables
    
    def visitVar(self, ctx: joiParser.VarContext):
        return self.visit(ctx.idOrPointerOrAddrId())
    
    def visitPointer(self, ctx: joiParser.PointerContext):
        varname = self.visit(ctx.idOrPointerOrAddrId())[1]
        return ['pointer', varname]
    
    def visitAddress_identifier(self, ctx: joiParser.Address_identifierContext):
        varname = ctx.IDENTIFIER().getText()
        return ['address_identifier', varname]

    def visitExpression(self, ctx:joiParser.ExpressionContext):
        # if(ctx.functionCall()):
        #     return self.visit(ctx.functionCall())
        if(ctx.logicalOrExpression()):
            return self.visit(ctx.logicalOrExpression())

    def visitLogicalOrExpression(self, ctx:joiParser.LogicalOrExpressionContext):
        loc = self.visit(ctx.logicalAndExpression(0))

        for i in range(1, len(ctx.logicalAndExpression())):
            self.visit(ctx.logicalAndExpression(i)) 
            self.instructions.append('OR') 

        return loc
            
    def visitLogicalAndExpression(self, ctx:joiParser.LogicalAndExpressionContext):
        lac = self.visit(ctx.rel_expr(0))

        for i in range(1, len(ctx.rel_expr())):
            self.visit(ctx.rel_expr(i))  
            self.instructions.append('AND') 
        return lac

    def visitRel_expr(self, ctx:joiParser.Rel_exprContext):
        # NOT rel_expr 
        if ctx.NOT():
            relexp = self.visit(ctx.rel_expr())  
            self.instructions.append('NOT')  
            return relexp
        else:
            e= self.visit(ctx.expr(0))
            
            for i in range(1, len(ctx.expr())):
                self.visit(ctx.expr(i))  
                comp_op = ctx.comparisonOp(i - 1).getText() 
                self.visitComparisonOp(comp_op)

            return e


    def visitExpr(self, ctx:joiParser.ExprContext):
        t = self.visit(ctx.term(0)) 
        
        for i in range(1, len(ctx.term())):
            self.visit(ctx.term(i))  
            op = ctx.getChild(2 * i - 1).getText()  
            
            if op == '+':
                self.instructions.append('ADD')  
            elif op == '-':
                self.instructions.append('SUB') 

        return t

    def visitTerm(self, ctx:joiParser.TermContext):
        f = self.visit(ctx.factor(0))  
        
        for i in range(1, len(ctx.factor())):
            self.visit(ctx.factor(i)) 
            op = ctx.getChild(2 * i - 1).getText()  
            if op == '*':
                self.instructions.append('MUL')
            elif op == '/':
                self.instructions.append('DIV')
            elif op == '%':
                self.instructions.append('MOD')
        
        return f

    def visitIdOrPointerOrAddrId(self, ctx: joiParser.IdOrPointerOrAddrIdContext):
        if(ctx.pointer()):
            return self.visit(ctx.pointer())
        elif(ctx.address_identifier()):
            return self.visit(ctx.address_identifier())
        return ['variable', ctx.IDENTIFIER().getText()]

    def visitFactor(self, ctx:joiParser.FactorContext):
        if ctx.idOrPointerOrAddrId():
            var_info = self.visit(ctx.idOrPointerOrAddrId())
            var_name = var_info[1]
            if(not symbolTable.read(var_name)):
                ExitFromProgram("cannot use undeclared variable")
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
            return var_info
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
            return self.visit(ctx.expr())  
        elif ctx.functionCall():
            self.visit(ctx.functionCall())
        elif ctx.structAccessStmt():
            self.visit(ctx.structAccessStmt())  # to be done



    def visitAssignStmt(self, ctx: joiParser.AssignStmtContext):

        # if ctx.IDENTIFIER() and ctx.expression(0) and ctx.expression(1):
        # (IDENTIFIER '[' expression ']' ('[' expression ']')* '=' expression ';')
        # should check this-------------------------------------
        if ctx.idOrPointerOrAddrId() and len(ctx.expression())>=2:
            var_name = self.visit(ctx.idOrPointerOrAddrId())[1]  
            if(not symbolTable.read(var_name)):
                ExitFromProgram("cannot assign to undeclared array")
            index = self.visit(ctx.expression(0))  
            
            for i in range(1, len(ctx.expression()) - 1):
                index = self.visit(ctx.expression(i)) 

            self.instructions.append(f'PUSH_ARRAY {var_name}')  
            self.instructions.append(f'PUSH {index}')  
            self.visit(ctx.expression(len(ctx.expression())-1))  
            self.instructions.append('POP_ARRAY') 
        elif ctx.idOrPointerOrAddrId() and ctx.expression(0) and not ctx.assignOp():
            var_name = self.visit(ctx.idOrPointerOrAddrId())[1] 
            if(not symbolTable.read(var_name)):
                ExitFromProgram("cannot assign to undeclared variable") 
            self.visit(ctx.expression(0))  
            self.instructions.append(f'STORE {var_name}')  
            self.instructions.append(f'POP {var_name}')  

        # (IDENTIFIER assignOp expression ';')
        elif ctx.idOrPointerOrAddrId() and ctx.assignOp() and ctx.expression(0):
            var_name = self.visit(ctx.idOrPointerOrAddrId())[1]
            if(not symbolTable.read(var_name)):
                ExitFromProgram("cannot assign to undeclared variable") 
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
            
    def visitStructDef(self, ctx: joiParser.StructDefContext):
        struct_name = ctx.IDENTIFIER().getText()
        if symbolTable.read(struct_name):
            ExitFromProgram(f"Struct '{struct_name}' already defined.")
        symbolTable.create(name=struct_name, symbol_type='struct', scope='ytd')

        for declaration in ctx.declarationStmt():
            self.visit(declaration)
            
    def visitStructDeclarationStmt(self, ctx: joiParser.StructDeclarationStmtContext):
        struct_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()
        if symbolTable.read(var_name):
            ExitFromProgram(f"Variable '{var_name}' already declared.")
        if not symbolTable.read(struct_name):
            ExitFromProgram(f"Struct '{struct_name}' is not defined.")
        symbolTable.create(name=var_name, symbol_type='struct', scope='ytd', datatype=struct_name)
        self.instructions.append(f'DECLARE {struct_name} {var_name}')
        
    def visitStructAccessStmt(self, ctx: joiParser.StructAccessStmtContext):
        struct_var = ctx.IDENTIFIER(0).getText()
        member = ctx.IDENTIFIER(1).getText()
        struct_info = symbolTable.read(struct_var)
        if not struct_info or struct_info['type'] != 'struct':
            ExitFromProgram(f"'{struct_var}' is not a struct variable.")
        member_info = symbolTable.read(f"{member}")
        if not member_info:
            ExitFromProgram(f"Struct '{struct_info['datatype']}' has no member '{member}'.")
        self.instructions.append(f'PUSH {struct_var}')
        self.instructions.append(f'PUSH_FIELD {member}')
        return (struct_var, member) 
        
        
    def visitStructAssignStmt(self, ctx: joiParser.StructAssignStmtContext):
        struct_access_info = self.visit(ctx.structAccessStmt())
        if struct_access_info is not None:  
            if ctx.expression():     
                for i, expr in enumerate(ctx.expression()):
                    self.visit(expr)
                self.instructions.append('POP_FIELD')     
            else:
                raise Exception(f"Unhandled struct assignment type: {ctx}")

    def visitMainFunction(self, ctx:joiParser.MainFunctionContext):
        self.instructions.append('LABEL MAIN')  
        self.visit(ctx.statements())  
        self.instructions.append('RETURN')  
        self.visit(ctx.expression())  
        self.instructions.append('HALT')  
        symbolTable.display()
