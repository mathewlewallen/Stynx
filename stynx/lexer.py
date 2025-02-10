# stynx/lexer.py
import re

TOKEN_REGEX = [
    (r'[ \t]+',              None),        
    (r'#.*',                 None),       
    (r'[A-Za-z_]\w*',        'IDENT'),     
    (r'\d+(\.\d+)?',         'NUMBER'),  
    (r'\(',                  'LPAREN'),
    (r'\)',                  'RPAREN'),
    (r'\,',                  'COMMA'),
    (r'\:',                  'COLON'),
    (r'\=',                  'EQ'),
    (r'\*',                  'MUL'),
    (r'\+',                  'PLUS'),
    (r'\-',                  'MINUS'),
    (r'print',               'PRINT'),
    (r'var',                 'VAR'),
    (r'grad',                'GRAD'),
    (r'tensor',              'TENSOR'),
]

def tokenize(line, line_num):
    """
    Tokenize a single line of input into a list of tuples:
        (token_type, text, line_number, col_start)
    """
    tokens = []
    i = 0
    while i < len(line):
        match_found = False
        for pattern, token_type in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(line, i)
            if match:
                match_text = match.group(0)
                col_start = i + 1  # 1-based column index

                if token_type:  
                    tokens.append((token_type, match_text, line_num, col_start))

                i += len(match_text)
                match_found = True
                break

        if not match_found:
            raise ValueError(
                f"Unexpected character '{line[i]}' on line {line_num}, column {i+1}"
            )
    return tokens

def lex_program(program_lines):
    """
    Convert a list of lines into a flat list of tokens with an added NEWLINE token at each line end.
    """
    all_tokens = []
    for line_idx, line in enumerate(program_lines, start=1):
        line = line.rstrip('\n')
        line_tokens = tokenize(line, line_idx)
        all_tokens.extend(line_tokens)
        all_tokens.append(('NEWLINE', '\\n', line_idx, len(line)+1))
    return all_tokens
