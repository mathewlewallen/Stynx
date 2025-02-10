import re

TOKEN_REGEX = [
    (r'[ \t]+', None),            
    (r'#.*', None),                 
    (r'\d+(\.\d+)?', 'NUMBER'),     
    (r'\bvar\b', 'VAR'),
    (r'\bprint\b', 'PRINT'),
    (r'\bgrad\b', 'GRAD'),
    (r'\btensor\b', 'TENSOR'),
    (r'[A-Za-z_]\w*', 'IDENT'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\,', 'COMMA'),
    (r'\:', 'COLON'),
    (r'\=', 'EQ'),
    (r'\*', 'MUL'),
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
]

def tokenize(source_code):

    tokens = []
    lines = source_code.splitlines()
    for line_num, line in enumerate(lines, start=1):
        pos = 0
        while pos < len(line):
            match_found = False
            for pattern, token_type in TOKEN_REGEX:
                regex = re.compile(pattern)
                match = regex.match(line, pos)
                if match:
                    lexeme = match.group(0)
                    if token_type is not None:
                        tokens.append((token_type, lexeme, line_num, pos + 1))
                    pos += len(lexeme)
                    match_found = True
                    break
            if not match_found:
                raise SyntaxError(f"Unexpected character '{line[pos]}' at line {line_num}, col {pos+1}")
        tokens.append(('NEWLINE', '\\n', line_num, len(line) + 1))
    tokens.append(('EOF', '', line_num + 1, 1))
    return tokens
