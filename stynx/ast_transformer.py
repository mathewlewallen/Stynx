from lark import Transformer, v_args
from stynx.ast_nodes import Number, BinOp, UnaryOp, Var, Assign, Print

@v_args(inline=True)
class ASTTransformer(Transformer):
    def number(self, token):
        return Number(token)
    
    def var(self, token):
        return Var(str(token))
    
    def add(self, left, right):
        return BinOp(left, '+', right)
    
    def sub(self, left, right):
        return BinOp(left, '-', right)
    
    def mul(self, left, right):
        return BinOp(left, '*', right)
    
    def div(self, left, right):
        return BinOp(left, '/', right)
    
    def neg(self, value):
        return UnaryOp('-', value)
    
    def assign(self, name, value):
        return Assign(str(name), value)
    
    def print_stmt(self, expr):
        return Print(expr)
    
    def start(self, *statements):
        return list(statements)
