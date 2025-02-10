class VarDeclNode:
    def __init__(self, var_name, type_annotation=None):
        self.var_name = var_name
        self.type_annotation = type_annotation
    def __repr__(self):
        if self.type_annotation:
            return f"VarDecl({self.var_name}: {self.type_annotation})"
        return f"VarDecl({self.var_name})"

class TensorDeclNode:
    def __init__(self, var_name, dims):
        self.var_name = var_name
        self.dims = dims  
    def __repr__(self):
        return f"TensorDecl({self.var_name}, dims={self.dims})"

class AssignNode:
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr
    def __repr__(self):
        return f"Assign({self.var_name} = {self.expr})"

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op  
        self.right = right
    def __repr__(self):
        return f"BinOp({self.left} {self.op} {self.right})"

class PrintNode:
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self):
        return f"Print({self.expr})"

class GradNode:
    def __init__(self, expr, wrt):
        self.expr = expr
        self.wrt = wrt
    def __repr__(self):
        return f"Grad({self.expr}, wrt={self.wrt})"

class NumberNode:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Number({self.value})"

class VarRefNode:
    def __init__(self, var_name):
        self.var_name = var_name
    def __repr__(self):
        return f"VarRef({self.var_name})"
