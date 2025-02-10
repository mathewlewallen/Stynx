# stynx/ast_nodes.py

class VarDeclNode:
    def __init__(self, var_name):
        self.var_name = var_name
    def __repr__(self):
        return f"VarDeclNode({self.var_name})"

class TensorDeclNode:
    """ var x: tensor(2,2) """
    def __init__(self, var_name, dims):
        self.var_name = var_name
        self.dims = dims 
    def __repr__(self):
        return f"TensorDeclNode({self.var_name}, dims={self.dims})"

class AssignNode:
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr
    def __repr__(self):
        return f"AssignNode({self.var_name} = {self.expr})"

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"BinOpNode({self.left} {self.op} {self.right})"

class PrintNode:
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self):
        return f"PrintNode({self.expr})"

class GradNode:
    """ grad(z, x) """
    def __init__(self, expr, wrt_var):
        self.expr = expr
        self.wrt_var = wrt_var
    def __repr__(self):
        return f"GradNode({self.expr}, wrt={self.wrt_var})"

class NumberNode:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"NumberNode({self.value})"

class VarRefNode:
    def __init__(self, var_name):
        self.var_name = var_name
    def __repr__(self):
        return f"VarRefNode({self.var_name})"
