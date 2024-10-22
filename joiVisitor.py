# Generated from joi.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .joiParser import joiParser
else:
    from joiParser import joiParser

# This class defines a complete generic visitor for a parse tree produced by joiParser.

class joiVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by joiParser#program.
    def visitProgram(self, ctx:joiParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#includeStmt.
    def visitIncludeStmt(self, ctx:joiParser.IncludeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#usingStmt.
    def visitUsingStmt(self, ctx:joiParser.UsingStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#functionDefOrStructDefOrEnumDef.
    def visitFunctionDefOrStructDefOrEnumDef(self, ctx:joiParser.FunctionDefOrStructDefOrEnumDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#functionDef.
    def visitFunctionDef(self, ctx:joiParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#classDef.
    def visitClassDef(self, ctx:joiParser.ClassDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#constructor.
    def visitConstructor(self, ctx:joiParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#paramList.
    def visitParamList(self, ctx:joiParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#param.
    def visitParam(self, ctx:joiParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#functionCall.
    def visitFunctionCall(self, ctx:joiParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#argList.
    def visitArgList(self, ctx:joiParser.ArgListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#mainFunction.
    def visitMainFunction(self, ctx:joiParser.MainFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#statements.
    def visitStatements(self, ctx:joiParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#statement.
    def visitStatement(self, ctx:joiParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#deleteStmt.
    def visitDeleteStmt(self, ctx:joiParser.DeleteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#structDef.
    def visitStructDef(self, ctx:joiParser.StructDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#enumDef.
    def visitEnumDef(self, ctx:joiParser.EnumDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#breakStmt.
    def visitBreakStmt(self, ctx:joiParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#continueStmt.
    def visitContinueStmt(self, ctx:joiParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#printStmt.
    def visitPrintStmt(self, ctx:joiParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#printExpressionList.
    def visitPrintExpressionList(self, ctx:joiParser.PrintExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#inputStmt.
    def visitInputStmt(self, ctx:joiParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#assignStmt.
    def visitAssignStmt(self, ctx:joiParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#structAssignStmt.
    def visitStructAssignStmt(self, ctx:joiParser.StructAssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#structAccessStmt.
    def visitStructAccessStmt(self, ctx:joiParser.StructAccessStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#classFunctionAccessStmt.
    def visitClassFunctionAccessStmt(self, ctx:joiParser.ClassFunctionAccessStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#returnStmt.
    def visitReturnStmt(self, ctx:joiParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#declarationStmt.
    def visitDeclarationStmt(self, ctx:joiParser.DeclarationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#arrayDeclarationStmt.
    def visitArrayDeclarationStmt(self, ctx:joiParser.ArrayDeclarationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#arrayValueAssigning.
    def visitArrayValueAssigning(self, ctx:joiParser.ArrayValueAssigningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#referenceDeclarationStmt.
    def visitReferenceDeclarationStmt(self, ctx:joiParser.ReferenceDeclarationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#constDeclarationStmt.
    def visitConstDeclarationStmt(self, ctx:joiParser.ConstDeclarationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#varList.
    def visitVarList(self, ctx:joiParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#tryCatchStmt.
    def visitTryCatchStmt(self, ctx:joiParser.TryCatchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#catchBlock.
    def visitCatchBlock(self, ctx:joiParser.CatchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#throwStmt.
    def visitThrowStmt(self, ctx:joiParser.ThrowStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#ifStmt.
    def visitIfStmt(self, ctx:joiParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#elseIfStmt.
    def visitElseIfStmt(self, ctx:joiParser.ElseIfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#elseStmt.
    def visitElseStmt(self, ctx:joiParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#switchStmt.
    def visitSwitchStmt(self, ctx:joiParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#caseStmt.
    def visitCaseStmt(self, ctx:joiParser.CaseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#defaultStmt.
    def visitDefaultStmt(self, ctx:joiParser.DefaultStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#whileStmt.
    def visitWhileStmt(self, ctx:joiParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:joiParser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#forStmt.
    def visitForStmt(self, ctx:joiParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#forInit.
    def visitForInit(self, ctx:joiParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#forUpdate.
    def visitForUpdate(self, ctx:joiParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:joiParser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#expression.
    def visitExpression(self, ctx:joiParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:joiParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:joiParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#rel_expr.
    def visitRel_expr(self, ctx:joiParser.Rel_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#expr.
    def visitExpr(self, ctx:joiParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#term.
    def visitTerm(self, ctx:joiParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#factor.
    def visitFactor(self, ctx:joiParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#condition.
    def visitCondition(self, ctx:joiParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#arithmeticOp.
    def visitArithmeticOp(self, ctx:joiParser.ArithmeticOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#assignOp.
    def visitAssignOp(self, ctx:joiParser.AssignOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#comparisonOp.
    def visitComparisonOp(self, ctx:joiParser.ComparisonOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#logicalOp.
    def visitLogicalOp(self, ctx:joiParser.LogicalOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#dataType.
    def visitDataType(self, ctx:joiParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#referenceDataType.
    def visitReferenceDataType(self, ctx:joiParser.ReferenceDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by joiParser#main.
    def visitMain(self, ctx:joiParser.MainContext):
        return self.visitChildren(ctx)



del joiParser