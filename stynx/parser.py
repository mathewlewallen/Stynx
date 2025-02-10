from .lexer import tokenize
from .ast_nodes import (
    VarDeclNode, TensorDeclNode, AssignNode, BinOpNode,
    PrintNode, GradNode, NumberNode, VarRefNode
)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def peek(self):
        return self.tokens[self.current]

    def is_at_end(self):
        return self.peek()[0] == 'EOF'

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def previous(self):
        return self.tokens[self.current - 1]

    def check(self, token_type):
        if self.is_at_end():
            return False
        return self.peek()[0] == token_type

    def match(self, *types):
        for token_type in types:
            if self.check(token_type):
                self.advance()
                return True
        return False

    def consume(self, token_type, message):
        if self.check(token_type):
            return self.advance()
        token = self.peek()
        raise SyntaxError(f"{message} at line {token[2]}, col {token[3]} (found {token[0]}: '{token[1]}')")

    def parse_program(self):
        statements = []
        while not self.is_at_end():
            while self.match('NEWLINE'):
                pass
            if self.is_at_end():
                break
            stmt = self.parse_statement()
            statements.append(stmt)
        return statements

    def parse_statement(self):
        if self.match('VAR'):
            return self.parse_var_decl()
        if self.match('PRINT'):
            return self.parse_print()
        if self.match('GRAD'):
            return self.parse_grad()
        return self.parse_assignment()

    def parse_var_decl(self):
        token = self.consume('IDENT', "Expected variable name after 'var'")
        var_name = token[1]
        # Optional type annotation.
        if self.match('COLON'):
            self.consume('TENSOR', "Expected 'tensor' after ':' in variable declaration")
            self.consume('LPAREN', "Expected '(' after 'tensor'")
            dims = []
            while not self.check('RPAREN'):
                num_token = self.consume('NUMBER', "Expected dimension number")
                dims.append(int(num_token[1]))
                if not self.check('RPAREN'):
                    self.consume('COMMA', "Expected ',' between dimensions")
            self.consume('RPAREN', "Expected ')' after dimensions")
            return TensorDeclNode(var_name, dims)
        else:
            return VarDeclNode(var_name)

    def parse_assignment(self):
        token = self.consume('IDENT', "Expected variable name for assignment")
        var_name = token[1]
        self.consume('EQ', "Expected '=' after variable name")
        expr = self.parse_expression()
        return AssignNode(var_name, expr)

    def parse_print(self):
        self.consume('LPAREN', "Expected '(' after 'print'")
        expr = self.parse_expression()
        self.consume('RPAREN', "Expected ')' after expression in print")
        return PrintNode(expr)

    def parse_grad(self):
        self.consume('LPAREN', "Expected '(' after 'grad'")
        expr = self.parse_expression()
        self.consume('COMMA', "Expected ',' in grad expression")
        token = self.consume('IDENT', "Expected variable name in grad expression")
        wrt = token[1]
        self.consume('RPAREN', "Expected ')' after grad expression")
        return GradNode(expr, wrt)

    def parse_expression(self):
        return self.parse_term()

    def parse_term(self):
        expr = self.parse_factor()
        while self.match('PLUS', 'MINUS'):
            operator = self.previous()[0]
            right = self.parse_factor()
            expr = BinOpNode(expr, operator, right)
        return expr

    def parse_factor(self):
        expr = self.parse_unary()
        while self.match('MUL'):
            operator = self.previous()[0] 
            right = self.parse_unary()
            expr = BinOpNode(expr, operator, right)
        return expr

    def parse_unary(self):
        if self.match('MINUS'):
            operator = self.previous()[0]  # 'MINUS'
            right = self.parse_unary()
            return BinOpNode(NumberNode(0), operator, right)
        return self.parse_primary()

    def parse_primary(self):
        if self.match('NUMBER'):
            return NumberNode(float(self.previous()[1]))
        if self.match('IDENT'):
            return VarRefNode(self.previous()[1])
        if self.match('LPAREN'):
            expr = self.parse_expression()
            self.consume('RPAREN', "Expected ')' after expression")
            return expr
        token = self.peek()
        raise SyntaxError(f"Unexpected token {token[0]} at line {token[2]}, col {token[3]}")

def parse_source(source_code):
    tokens = tokenize(source_code)
    parser = Parser(tokens)
    return parser.parse_program()
