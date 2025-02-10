from lark import Lark
from stynx.ast_transformer import ASTTransformer

def parse_code(source_code: str):
    with open("stynx/my_lang.lark", "r") as f:
        grammar = f.read()
    
    parser = Lark(grammar, parser="lalr", transformer=ASTTransformer())
    
    ast = parser.parse(source_code)
    return ast

if __name__ == "__main__":
    sample_code = """
    x = 3 + 4 * 2
    print x
    """
    
    ast = parse_code(sample_code)
    print("Generated AST:")
    for node in ast:
        print(node)