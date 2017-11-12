# Package tokenizer performs lexical analysis of converting Cygnus code into readable tokens
import ply.lex as lex

class TokenizerException(Exception):
    pass

# PLY uses regular expressions to match symbols to proper tokens

# Syntactic keywords
keywords = {
    'if' : 'IF',
    'else' : 'ELSE',
    'elif' : 'ELIF',
    'done' : 'DONE',
    'return' : 'RETURN',
    'let' : 'LET',
    'int': 'INTTYPE',
    'float': 'FLOATTYPE',
    'char': 'CHARTYPE',
    'function': 'FUNCTIONTYPE'
}

# List of tokens legal to Cygnus
tokens = [
    'INT', 'FLOAT','PLUS', 'MULTI', 'DIV', 'SUB', 'NAME', 'LPAREN', 'RPAREN', 'COLON', 'COMMA',
    'SEMICOLON', 'ARROW', 'EQUALS', 'OCT', 'HEX', 'GT', 'LT', 'GTE', 'LTE'
] + list(keywords.values())

# Patterns for every token defined by either a function or regular expression
# Regular expressions for legal tokens
t_INT = r'-?[1-9]+[0-9]*'
t_HEX = r'0x[0-9a-fA-F]*'
t_OCT = r'0[0-9]*'
t_FLOAT = r'-?[0-9]*\.[0-9]+'
t_PLUS = r'\+'
t_MULTI = r'\*'
t_DIV = r'\/'
t_SUB = r'-'
# t_NAME = r'[a-zA-Z_]+([a-zA-Z0-9_])*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r'\:'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_ARROW = r'\-\>'
t_EQUALS = r'='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_ignore = ' \t'

tokenizer = lex.lex()

def t_NAME(token):
    r'\b[a-zA-Z_]+([a-zA-Z0-9_])*\b'
    print('this is a name:', token.value)
    token.type = keywords.get(token.value, 'NAME')
    return token

def t_NEWLINE(token):
    r'\n+'
    token.tokenizer.lineno += len(token.value)

def t_BLOCKCOMMENT(token):
    r'/\*(.|\n)*\*/'
    pass

def t_COMMENT(token):
    r'//.*'
    pass

def t_exception(token):
    print("Illegal character '%s'" % token.value[0])
    raise TokenizerException()

# pre :
# post : returns a list of tokens from a given string of data
def lex(data):
    tokenizer.input(data)
    # Tokenize
    tokens = []
    loop = True
    while loop:
        tok = tokenizer.token()
        if not tok:
            loop = False
        else:
            tokens.append(tok)
    return tokens




