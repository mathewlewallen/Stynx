# stynx/parser.py

from .ast_nodes import (
    VarDeclNode, TensorDeclNode, AssignNode, BinOpNode,
    PrintNode, GradNode, NumberNode, VarRefNode
)
from .lexer import lex_program

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens  
        self.pos = 0
    
    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return (None, None, -1, -1)
    
    def advance(self):
        self.pos += 1
    
    def match(self, token_type):
        ttype, ttext, line, col = self.current_token()
        if ttype == token_type:
            self.advance()
            return True
        return False
    
    def expect(self, token_type):
        ttype, ttext, line, col = self.current_token()
        if ttype == token_type:
            self.advance()
            return (ttype, ttext, line, col)
        raise SyntaxError(f"Expected {token_type}, got {ttype} at line {line}, col {col}.")
    
    def parse_program(self):
        statements = []
        while self.current_token()[0] is not None:
            if self.current_token()[0] == 'NEWLINE':
                self.advance()
                continue
            
            stmt = self.parse_statement()
            statements.append(stmt)
        return statements
    
    def parse_statement(self):
        ttype, ttext, line, col = self.current_token()
        
        if ttype == 'VAR':
            return self.parse_var_decl()
        elif ttype == 'IDENT':
            # likely an assignment: x = expr
            return self.parse_assignment()
        elif ttype == 'PRINT':
            return self.parse_print()
        elif ttype == 'GRAD':
            return self.parse_grad()
        else:
            raise SyntaxError(f"Unexpected token '{ttext}' of type {ttype} at line {line}, col {col}")
    
    def parse_var_decl(self):
        self.expect('VAR')
        ttype, var_name, line, col = self.expect('IDENT')
        
        if self.match('COLON'):
            self.expect('TENSOR')   
            self.expect('LPAREN') 
            dims = []
            while not self.match('RPAREN'):
                token_type, token_text, l, c = self.expect('NUMBER')
                dims.append(token_text)
                self.match('COMMA')  
            return TensorDeclNode(var_name, dims)
        else:
            return VarDeclNode(var_name)
    
    def parse_assignment(self):
        ttype, var_name, line, col = self.expect('IDENT')
        self.expect('EQ')
        expr = self.parse_expression()
        return AssignNode(var_name, expr)
    
    def parse_print(self):
        self.expect('PRINT')
        self.expect('LPAREN')
        expr = self.parse_expression()
        self.expect('RPAREN')
        return PrintNode(expr)
    
    def parse_grad(self):
        self.expect('GRAD')
        self.expect('LPAREN')
        expr = self.parse_expression()
        self.expect('COMMA')
        ttype, wrt_name, line, col = self.expect('IDENT')
        self.expect('RPAREN')
        return GradNode(expr, wrt_name)
    
    def parse_expression(self):
        left = self.parse_factor()
        while True:
            ttype, ttext, line, col = self.current_token()
            if ttype in ('PLUS', 'MINUS', 'MUL'):
                op = ttype
                self.advance()
                right = self.parse_factor()
                left = BinOpNode(left, op, right)
            else:
                break
        return left
    
    def parse_factor(self):
        ttype, ttext, line, col = self.current_token()
        if ttype == 'NUMBER':
            self.advance()
            return NumberNode(float(ttext))
        elif ttype == 'IDENT':
            self.advance()
            return VarRefNode(ttext)
        else:
            raise SyntaxError(f"Unexpected token '{ttext}' at line {line}, col {col}")

def parse_source(program_lines):
    tokens = lex_program(program_lines)
    parser = Parser(tokens)
    return parser.parse_program()
