import numpy as np
from .ast_nodes import VarDeclNode, TensorDeclNode, AssignNode, BinOpNode, PrintNode, GradNode, NumberNode, VarRefNode
from .autodiff import evaluate_expression, compute_gradient

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
            self.env[stmt.var_name] = np.zeros(stmt.dims)
        elif isinstance(stmt, AssignNode):
            value = self.evaluate(stmt.expr)
            self.env[stmt.var_name] = value
        elif isinstance(stmt, PrintNode):
            value = self.evaluate(stmt.expr)
            if isinstance(value, float) and value.is_integer():
                print(int(value))
            else:
                print(value)
        elif isinstance(stmt, GradNode):
            grad_val = compute_gradient(stmt.expr, stmt.wrt, self.env)
            print(f"Gradient of {stmt.expr} with respect to {stmt.wrt}: {grad_val}")
        else:
            raise RuntimeError(f"Unknown statement type: {stmt}")

    def evaluate(self, expr):
        if isinstance(expr, NumberNode):
            return expr.value
        elif isinstance(expr, VarRefNode):
            return self.env.get(expr.var_name, 0)
        elif isinstance(expr, BinOpNode):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)
            if expr.op == 'PLUS':
                return left + right
            elif expr.op == 'MINUS':
                return left - right
            elif expr.op == 'MUL':
                return left * right
            else:
                raise NotImplementedError(f"Operator {expr.op} not implemented.")
        else:
            raise NotImplementedError("Expression type not implemented.")
