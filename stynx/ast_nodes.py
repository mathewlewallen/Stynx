class ASTNode:
    pass

class Number(ASTNode):
    def __init__(self, value):
        self.value = float(value)  
    def __repr__(self):
        return f"Number({self.value})"

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left    
        self.op = op        
        self.right = right  
    def __repr__(self):
        return f"BinOp({self.left}, '{self.op}', {self.right})"

class UnaryOp(ASTNode):
    def __init__(self, op, operand):
        self.op = op          
        self.operand = operand  
    def __repr__(self):
        return f"UnaryOp('{self.op}', {self.operand})"

# Node for variables
class Var(ASTNode):
    def __init__(self, name):
        self.name = name    
    def __repr__(self):
        return f"Var('{self.name}')"

# Node for assignments
class Assign(ASTNode):
    def __init__(self, name, value):
        self.name = name     
        self.value = value  
    def __repr__(self):
        return f"Assign(Var('{self.name}'), {self.value})"

# Node for print statements
class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr     
    def __repr__(self):
        return f"Print({self.expr})"
