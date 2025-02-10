from lark import Lark
from ast_transformer import ASTTransformer

def parse_code(source_code: str):
    with open("my_lang.lark", "r") as f:
        grammar = f.read()
    
    parser = Lark(grammar, parser="lalr", transformer=ASTTransformer())
    
    ast = parser.parse(source_code)
    return ast

if __name__ == "__main__":
    source = """
    x = 3 + 4 * 2
    print x
    """
    
    ast = parse_code(source)
    print("Generated AST:")
    for node in ast:
        print(node)
