import pytest
from stynx.parser import parse_code
from stynx.ast_nodes import Assign, BinOp, Number, Var, Print

def test_assignment_and_print():
    source_code = """
    x = 3 + 4 * 2
    print x
    """
    ast = parse_code(source_code)
    
    assert len(ast) == 2
    
    # Verify the assignment statement
    assign_node = ast[0]
    assert isinstance(assign_node, Assign)
    assert assign_node.name == "x"
    
    binop_node = assign_node.value
    assert isinstance(binop_node, BinOp)
    assert binop_node.op == "+"
    assert isinstance(binop_node.left, Number)
    assert binop_node.left.value == 3.0
    right_node = binop_node.right
    assert isinstance(right_node, BinOp)
    assert right_node.op == "*"
    
    print_node = ast[1]
    assert isinstance(print_node, Print)
    assert isinstance(print_node.expr, Var)
    assert print_node.expr.name == "x"
