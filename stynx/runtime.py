# stynx/runtime.py

import numpy as np
from .ast_nodes import (
    VarDeclNode, TensorDeclNode, AssignNode, BinOpNode,
    PrintNode, GradNode, NumberNode, VarRefNode
)
from .autodiff import compute_gradient, evaluate_expression

class Runtime:
    def __init__(self):
        self.env = {}
    
    def run_statements(self, statements):
        for stmt in statements:
            self.execute(stmt)
    
    def execute(self, stmt):
        if isinstance(stmt, VarDeclNode):
            self.env[stmt.var_name] = None
        
        elif isinstance(stmt, TensorDeclNode):
            # e.g. var x: tensor(2,2)
            dims = [int(d) for d in stmt.dims]
            self.env[stmt.var_name] = np.zeros(dims) 
        
        elif isinstance(stmt, AssignNode):
            val = self.eval_expr(stmt.expr)
            self.env[stmt.var_name] = val
        
        elif isinstance(stmt, PrintNode):
            val = self.eval_expr(stmt.expr)
            print(val)
        
        elif isinstance(stmt, GradNode):
            grad_val = compute_gradient(stmt.expr, stmt.wrt_var, self.env)
            print(f"d({stmt.expr})/d({stmt.wrt_var}) = {grad_val}")
        
        else:
            raise ValueError(f"Unknown statement type: {stmt}")
    
    def eval_expr(self, expr):
        # Reuse the evaluate_expression from autodiff
        return evaluate_expression(expr, self.env)
