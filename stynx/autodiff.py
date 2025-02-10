from .ast_nodes import NumberNode, VarRefNode, BinOpNode

def evaluate_expression(expr, env):
    if isinstance(expr, NumberNode):
        return expr.value
    elif isinstance(expr, VarRefNode):
        return env.get(expr.var_name, 0)
    elif isinstance(expr, BinOpNode):
        left = evaluate_expression(expr.left, env)
        right = evaluate_expression(expr.right, env)
        if expr.op == 'PLUS':
            return left + right
        elif expr.op == 'MINUS':
            return left - right
        elif expr.op == 'MUL':
            return left * right
        else:
            raise NotImplementedError(f"Operator {expr.op} not supported.")
    else:
        raise NotImplementedError("Expression type not supported.")

def compute_gradient(expr, wrt, env):
    if isinstance(expr, NumberNode):
        return 0
    elif isinstance(expr, VarRefNode):
        return 1 if expr.var_name == wrt else 0
    elif isinstance(expr, BinOpNode):
        left_grad = compute_gradient(expr.left, wrt, env)
        right_grad = compute_gradient(expr.right, wrt, env)
        left_val = evaluate_expression(expr.left, env)
        right_val = evaluate_expression(expr.right, env)
        if expr.op == 'PLUS':
            return left_grad + right_grad
        elif expr.op == 'MINUS':
            return left_grad - right_grad
        elif expr.op == 'MUL':
            return left_val * right_grad + right_val * left_grad
        else:
            raise NotImplementedError(f"Operator {expr.op} not supported in grad.")
    else:
        raise NotImplementedError("Expression type not supported in grad.")
