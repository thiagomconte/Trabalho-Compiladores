# calclex.py
from sly import Lexer

class CalcLexer(Lexer):
    # Set of token names. This is always required 

    tokens = { ID, NUM, PLUS, MINUS, TIMES,
               DIVIDE, EQUAL, AND, LESS,
               KEYWORD, SCOLON, COLON, LPAREN, LBRACK, RBRACK,
               RPAREN, LBRACE, RBRACE, DOT, NOT, WRITE }
    
    
    # String containing ignored characters between tokens
    ignore = ' \t'
    ignore_newline = r'\n+'
    
    # Regular expression rules for tokens
    ID['System.out.println'] = KEYWORD
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = KEYWORD
    ID['while'] = KEYWORD
    ID['else'] = KEYWORD
    ID['return'] = KEYWORD
    ID['class'] = KEYWORD
    ID['int'] = KEYWORD
    ID['public'] = KEYWORD
    ID['private'] = KEYWORD
    ID['static'] = KEYWORD
    ID['void'] = KEYWORD
    ID['main'] = KEYWORD
    ID['extends'] = KEYWORD
    ID['boolean'] = KEYWORD
    ID['true'] = KEYWORD
    ID['false'] = KEYWORD
    ID['this'] = KEYWORD
    ID['new'] = KEYWORD
    ID['length'] = KEYWORD
    SCOLON = r'\;'
    COLON = r'\,'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'
    LBRACK = r'\['
    RBRACK = r'\]'
    DOT = r'\.'
    NOT = r'!'
    NUM  = r'\d+'
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQUAL  = r'='
    AND = r'&&'
    LESS = r'<'
    
    #AÇÃO PARA DETECTAR QUEBRA DE LINHA E INCREMENTÁ-LA
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
    
    def error(self, t):
        print("Linha %d - Caractere ilegal : %s" % (t.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
    file = input('Nome do arquivo > ')
    myfile = open(file, 'r')
    data = myfile.read()
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('[%r , %r , %r]' % (tok.lineno, tok.type, tok.value))
    myfile.close()    