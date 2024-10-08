# Generated from joi.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .joiParser import joiParser
else:
    from joiParser import joiParser

# This class defines a complete listener for a parse tree produced by joiParser.
class joiListener(ParseTreeListener):

    # Enter a parse tree produced by joiParser#program.
    def enterProgram(self, ctx:joiParser.ProgramContext):
        pass

    # Exit a parse tree produced by joiParser#program.
    def exitProgram(self, ctx:joiParser.ProgramContext):
        pass


    # Enter a parse tree produced by joiParser#includeStmt.
    def enterIncludeStmt(self, ctx:joiParser.IncludeStmtContext):
        pass

    # Exit a parse tree produced by joiParser#includeStmt.
    def exitIncludeStmt(self, ctx:joiParser.IncludeStmtContext):
        pass


    # Enter a parse tree produced by joiParser#usingStmt.
    def enterUsingStmt(self, ctx:joiParser.UsingStmtContext):
        pass

    # Exit a parse tree produced by joiParser#usingStmt.
    def exitUsingStmt(self, ctx:joiParser.UsingStmtContext):
        pass


    # Enter a parse tree produced by joiParser#functionDefOrStructDefOrEnumDef.
    def enterFunctionDefOrStructDefOrEnumDef(self, ctx:joiParser.FunctionDefOrStructDefOrEnumDefContext):
        pass

    # Exit a parse tree produced by joiParser#functionDefOrStructDefOrEnumDef.
    def exitFunctionDefOrStructDefOrEnumDef(self, ctx:joiParser.FunctionDefOrStructDefOrEnumDefContext):
        pass


    # Enter a parse tree produced by joiParser#functionDef.
    def enterFunctionDef(self, ctx:joiParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by joiParser#functionDef.
    def exitFunctionDef(self, ctx:joiParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by joiParser#classDef.
    def enterClassDef(self, ctx:joiParser.ClassDefContext):
        pass

    # Exit a parse tree produced by joiParser#classDef.
    def exitClassDef(self, ctx:joiParser.ClassDefContext):
        pass


    # Enter a parse tree produced by joiParser#constructor.
    def enterConstructor(self, ctx:joiParser.ConstructorContext):
        pass

    # Exit a parse tree produced by joiParser#constructor.
    def exitConstructor(self, ctx:joiParser.ConstructorContext):
        pass


    # Enter a parse tree produced by joiParser#paramList.
    def enterParamList(self, ctx:joiParser.ParamListContext):
        pass

    # Exit a parse tree produced by joiParser#paramList.
    def exitParamList(self, ctx:joiParser.ParamListContext):
        pass


    # Enter a parse tree produced by joiParser#param.
    def enterParam(self, ctx:joiParser.ParamContext):
        pass

    # Exit a parse tree produced by joiParser#param.
    def exitParam(self, ctx:joiParser.ParamContext):
        pass


    # Enter a parse tree produced by joiParser#functionCall.
    def enterFunctionCall(self, ctx:joiParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by joiParser#functionCall.
    def exitFunctionCall(self, ctx:joiParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by joiParser#argList.
    def enterArgList(self, ctx:joiParser.ArgListContext):
        pass

    # Exit a parse tree produced by joiParser#argList.
    def exitArgList(self, ctx:joiParser.ArgListContext):
        pass


    # Enter a parse tree produced by joiParser#mainFunction.
    def enterMainFunction(self, ctx:joiParser.MainFunctionContext):
        pass

    # Exit a parse tree produced by joiParser#mainFunction.
    def exitMainFunction(self, ctx:joiParser.MainFunctionContext):
        pass


    # Enter a parse tree produced by joiParser#statements.
    def enterStatements(self, ctx:joiParser.StatementsContext):
        pass

    # Exit a parse tree produced by joiParser#statements.
    def exitStatements(self, ctx:joiParser.StatementsContext):
        pass


    # Enter a parse tree produced by joiParser#statement.
    def enterStatement(self, ctx:joiParser.StatementContext):
        pass

    # Exit a parse tree produced by joiParser#statement.
    def exitStatement(self, ctx:joiParser.StatementContext):
        pass


    # Enter a parse tree produced by joiParser#structDef.
    def enterStructDef(self, ctx:joiParser.StructDefContext):
        pass

    # Exit a parse tree produced by joiParser#structDef.
    def exitStructDef(self, ctx:joiParser.StructDefContext):
        pass


    # Enter a parse tree produced by joiParser#enumDef.
    def enterEnumDef(self, ctx:joiParser.EnumDefContext):
        pass

    # Exit a parse tree produced by joiParser#enumDef.
    def exitEnumDef(self, ctx:joiParser.EnumDefContext):
        pass


    # Enter a parse tree produced by joiParser#breakStmt.
    def enterBreakStmt(self, ctx:joiParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by joiParser#breakStmt.
    def exitBreakStmt(self, ctx:joiParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by joiParser#continueStmt.
    def enterContinueStmt(self, ctx:joiParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by joiParser#continueStmt.
    def exitContinueStmt(self, ctx:joiParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by joiParser#printStmt.
    def enterPrintStmt(self, ctx:joiParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by joiParser#printStmt.
    def exitPrintStmt(self, ctx:joiParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by joiParser#printExpressionList.
    def enterPrintExpressionList(self, ctx:joiParser.PrintExpressionListContext):
        pass

    # Exit a parse tree produced by joiParser#printExpressionList.
    def exitPrintExpressionList(self, ctx:joiParser.PrintExpressionListContext):
        pass


    # Enter a parse tree produced by joiParser#inputStmt.
    def enterInputStmt(self, ctx:joiParser.InputStmtContext):
        pass

    # Exit a parse tree produced by joiParser#inputStmt.
    def exitInputStmt(self, ctx:joiParser.InputStmtContext):
        pass


    # Enter a parse tree produced by joiParser#assignStmt.
    def enterAssignStmt(self, ctx:joiParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by joiParser#assignStmt.
    def exitAssignStmt(self, ctx:joiParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by joiParser#structAssignStmt.
    def enterStructAssignStmt(self, ctx:joiParser.StructAssignStmtContext):
        pass

    # Exit a parse tree produced by joiParser#structAssignStmt.
    def exitStructAssignStmt(self, ctx:joiParser.StructAssignStmtContext):
        pass


    # Enter a parse tree produced by joiParser#structAccessStmt.
    def enterStructAccessStmt(self, ctx:joiParser.StructAccessStmtContext):
        pass

    # Exit a parse tree produced by joiParser#structAccessStmt.
    def exitStructAccessStmt(self, ctx:joiParser.StructAccessStmtContext):
        pass


    # Enter a parse tree produced by joiParser#returnStmt.
    def enterReturnStmt(self, ctx:joiParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by joiParser#returnStmt.
    def exitReturnStmt(self, ctx:joiParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by joiParser#declarationStmt.
    def enterDeclarationStmt(self, ctx:joiParser.DeclarationStmtContext):
        pass

    # Exit a parse tree produced by joiParser#declarationStmt.
    def exitDeclarationStmt(self, ctx:joiParser.DeclarationStmtContext):
        pass


    # Enter a parse tree produced by joiParser#arrayDeclarationStmt.
    def enterArrayDeclarationStmt(self, ctx:joiParser.ArrayDeclarationStmtContext):
        pass

    # Exit a parse tree produced by joiParser#arrayDeclarationStmt.
    def exitArrayDeclarationStmt(self, ctx:joiParser.ArrayDeclarationStmtContext):
        pass


    # Enter a parse tree produced by joiParser#arrayValueAssigning.
    def enterArrayValueAssigning(self, ctx:joiParser.ArrayValueAssigningContext):
        pass

    # Exit a parse tree produced by joiParser#arrayValueAssigning.
    def exitArrayValueAssigning(self, ctx:joiParser.ArrayValueAssigningContext):
        pass


    # Enter a parse tree produced by joiParser#referenceDeclarationStmt.
    def enterReferenceDeclarationStmt(self, ctx:joiParser.ReferenceDeclarationStmtContext):
        pass

    # Exit a parse tree produced by joiParser#referenceDeclarationStmt.
    def exitReferenceDeclarationStmt(self, ctx:joiParser.ReferenceDeclarationStmtContext):
        pass


    # Enter a parse tree produced by joiParser#constDeclarationStmt.
    def enterConstDeclarationStmt(self, ctx:joiParser.ConstDeclarationStmtContext):
        pass

    # Exit a parse tree produced by joiParser#constDeclarationStmt.
    def exitConstDeclarationStmt(self, ctx:joiParser.ConstDeclarationStmtContext):
        pass


    # Enter a parse tree produced by joiParser#varList.
    def enterVarList(self, ctx:joiParser.VarListContext):
        pass

    # Exit a parse tree produced by joiParser#varList.
    def exitVarList(self, ctx:joiParser.VarListContext):
        pass


    # Enter a parse tree produced by joiParser#ifStmt.
    def enterIfStmt(self, ctx:joiParser.IfStmtContext):
        pass

    # Exit a parse tree produced by joiParser#ifStmt.
    def exitIfStmt(self, ctx:joiParser.IfStmtContext):
        pass


    # Enter a parse tree produced by joiParser#elseIfStmt.
    def enterElseIfStmt(self, ctx:joiParser.ElseIfStmtContext):
        pass

    # Exit a parse tree produced by joiParser#elseIfStmt.
    def exitElseIfStmt(self, ctx:joiParser.ElseIfStmtContext):
        pass


    # Enter a parse tree produced by joiParser#elseStmt.
    def enterElseStmt(self, ctx:joiParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by joiParser#elseStmt.
    def exitElseStmt(self, ctx:joiParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by joiParser#switchStmt.
    def enterSwitchStmt(self, ctx:joiParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by joiParser#switchStmt.
    def exitSwitchStmt(self, ctx:joiParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by joiParser#caseStmt.
    def enterCaseStmt(self, ctx:joiParser.CaseStmtContext):
        pass

    # Exit a parse tree produced by joiParser#caseStmt.
    def exitCaseStmt(self, ctx:joiParser.CaseStmtContext):
        pass


    # Enter a parse tree produced by joiParser#defaultStmt.
    def enterDefaultStmt(self, ctx:joiParser.DefaultStmtContext):
        pass

    # Exit a parse tree produced by joiParser#defaultStmt.
    def exitDefaultStmt(self, ctx:joiParser.DefaultStmtContext):
        pass


    # Enter a parse tree produced by joiParser#whileStmt.
    def enterWhileStmt(self, ctx:joiParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by joiParser#whileStmt.
    def exitWhileStmt(self, ctx:joiParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by joiParser#doWhileStmt.
    def enterDoWhileStmt(self, ctx:joiParser.DoWhileStmtContext):
        pass

    # Exit a parse tree produced by joiParser#doWhileStmt.
    def exitDoWhileStmt(self, ctx:joiParser.DoWhileStmtContext):
        pass


    # Enter a parse tree produced by joiParser#forStmt.
    def enterForStmt(self, ctx:joiParser.ForStmtContext):
        pass

    # Exit a parse tree produced by joiParser#forStmt.
    def exitForStmt(self, ctx:joiParser.ForStmtContext):
        pass


    # Enter a parse tree produced by joiParser#forInit.
    def enterForInit(self, ctx:joiParser.ForInitContext):
        pass

    # Exit a parse tree produced by joiParser#forInit.
    def exitForInit(self, ctx:joiParser.ForInitContext):
        pass


    # Enter a parse tree produced by joiParser#forUpdate.
    def enterForUpdate(self, ctx:joiParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by joiParser#forUpdate.
    def exitForUpdate(self, ctx:joiParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by joiParser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:joiParser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by joiParser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:joiParser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by joiParser#expression.
    def enterExpression(self, ctx:joiParser.ExpressionContext):
        pass

    # Exit a parse tree produced by joiParser#expression.
    def exitExpression(self, ctx:joiParser.ExpressionContext):
        pass


    # Enter a parse tree produced by joiParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:joiParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by joiParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:joiParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by joiParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:joiParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by joiParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:joiParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by joiParser#rel_expr.
    def enterRel_expr(self, ctx:joiParser.Rel_exprContext):
        pass

    # Exit a parse tree produced by joiParser#rel_expr.
    def exitRel_expr(self, ctx:joiParser.Rel_exprContext):
        pass


    # Enter a parse tree produced by joiParser#expr.
    def enterExpr(self, ctx:joiParser.ExprContext):
        pass

    # Exit a parse tree produced by joiParser#expr.
    def exitExpr(self, ctx:joiParser.ExprContext):
        pass


    # Enter a parse tree produced by joiParser#term.
    def enterTerm(self, ctx:joiParser.TermContext):
        pass

    # Exit a parse tree produced by joiParser#term.
    def exitTerm(self, ctx:joiParser.TermContext):
        pass


    # Enter a parse tree produced by joiParser#factor.
    def enterFactor(self, ctx:joiParser.FactorContext):
        pass

    # Exit a parse tree produced by joiParser#factor.
    def exitFactor(self, ctx:joiParser.FactorContext):
        pass


    # Enter a parse tree produced by joiParser#condition.
    def enterCondition(self, ctx:joiParser.ConditionContext):
        pass

    # Exit a parse tree produced by joiParser#condition.
    def exitCondition(self, ctx:joiParser.ConditionContext):
        pass


    # Enter a parse tree produced by joiParser#arithmeticOp.
    def enterArithmeticOp(self, ctx:joiParser.ArithmeticOpContext):
        pass

    # Exit a parse tree produced by joiParser#arithmeticOp.
    def exitArithmeticOp(self, ctx:joiParser.ArithmeticOpContext):
        pass


    # Enter a parse tree produced by joiParser#comparisonOp.
    def enterComparisonOp(self, ctx:joiParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by joiParser#comparisonOp.
    def exitComparisonOp(self, ctx:joiParser.ComparisonOpContext):
        pass


    # Enter a parse tree produced by joiParser#logicalOp.
    def enterLogicalOp(self, ctx:joiParser.LogicalOpContext):
        pass

    # Exit a parse tree produced by joiParser#logicalOp.
    def exitLogicalOp(self, ctx:joiParser.LogicalOpContext):
        pass


    # Enter a parse tree produced by joiParser#dataType.
    def enterDataType(self, ctx:joiParser.DataTypeContext):
        pass

    # Exit a parse tree produced by joiParser#dataType.
    def exitDataType(self, ctx:joiParser.DataTypeContext):
        pass


    # Enter a parse tree produced by joiParser#referenceDataType.
    def enterReferenceDataType(self, ctx:joiParser.ReferenceDataTypeContext):
        pass

    # Exit a parse tree produced by joiParser#referenceDataType.
    def exitReferenceDataType(self, ctx:joiParser.ReferenceDataTypeContext):
        pass


    # Enter a parse tree produced by joiParser#main.
    def enterMain(self, ctx:joiParser.MainContext):
        pass

    # Exit a parse tree produced by joiParser#main.
    def exitMain(self, ctx:joiParser.MainContext):
        pass



del joiParser