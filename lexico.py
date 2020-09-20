# calclex.py
from sly import Lexer

class CalcLexer(Lexer):
    # Set of token names. This is always required 
    tokens = { ID, NUMBER, PLUS, MINUS, TIMES,
               DIVIDE, ASSIGN, AND, LT, LE,
               IF, WHILE, ELSE, RETURN, CLASS, PRINT, INT, METH }
    
    
    literals = {'(', ')', '{', '}', ';', '[', ']', '.'}
    
    # String containing ignored characters between tokens
    ignore = ' \t'
    
    # Regular expression rules for tokens
    PRINT = r'System.out.println'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['while'] = WHILE
    ID['else'] = ELSE
    ID['return'] = RETURN
    ID['class'] = CLASS
    ID['int'] = INT
    ID['public'] = METH
    NUMBER  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    ASSIGN  = r'='
    AND = r'&&'
    LE = r'<='
    LT = r'<'
    

if __name__ == '__main__':
    data = input('lex > ') 
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r lineno=%r index=%r' % (tok.type, tok.value, tok.lineno, tok.index))