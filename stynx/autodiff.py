# stynx/autodiff.py

import numpy as np

def compute_gradient(expr, wrt_var, env):
    """
    A naive gradient function for an expression (z) wrt a variable (x).
    'env' is a dict of var -> value, typically numpy arrays.
    This function returns d(expr)/d(wrt_var).
    """

    # (BinOpNode with +, -, * for demonstration.)
    from .ast_nodes import BinOpNode, NumberNode, VarRefNode

    if isinstance(expr, NumberNode):
        return 0.0

    if isinstance(expr, VarRefNode):
        return 1.0 if expr.var_name == wrt_var else 0.0

    if isinstance(expr, BinOpNode):
        left_grad = compute_gradient(expr.left, wrt_var, env)
        right_grad = compute_gradient(expr.right, wrt_var, env)

        left_val = evaluate_expression(expr.left, env)
        right_val = evaluate_expression(expr.right, env)

        if expr.op == 'PLUS':
            return left_grad + right_grad
        elif expr.op == 'MINUS':
            return left_grad - right_grad
        elif expr.op == 'MUL':
            return left_val * right_grad + right_val * left_grad
        else:
            raise NotImplementedError(f"Operator {expr.op} not supported in AD.")
    else:
        raise NotImplementedError("Expression not supported in autodiff")

def evaluate_expression(expr, env):
    """Helper that returns the numeric value of expr given an env."""
    from .ast_nodes import BinOpNode, NumberNode, VarRefNode
    if isinstance(expr, NumberNode):
        return expr.value
    if isinstance(expr, VarRefNode):
        return env[expr.var_name]
    if isinstance(expr, BinOpNode):
        left_val = evaluate_expression(expr.left, env)
        right_val = evaluate_expression(expr.right, env)
        if expr.op == 'PLUS':
            return left_val + right_val
        elif expr.op == 'MINUS':
            return left_val - right_val
        elif expr.op == 'MUL':
            return left_val * right_val
        else:
            raise NotImplementedError(f"Operator {expr.op} not supported.")
    else:
        raise NotImplementedError("Unhandled expression in evaluate_expression")
