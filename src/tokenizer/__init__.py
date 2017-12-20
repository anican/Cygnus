# Package tokenizer performs lexical analysis of converting Cygnus code into readable tokens
import ply.lex as lex

# class Tokenizer
class TokenizerException(Exception):
    pass

# PLY uses regular expressions to match symbols to proper tokens

# Syntactic keywords
keywords = {
   'if' : 'IF',
   'else' : 'ELSE',
   'done' : "DONE",
   'return': "RETURN",
   'const' : 'CONST',
   'let': 'LET',
   'int': 'INTTYPE',
   'float': 'FLOATTYPE',
   'char': 'CHARTYPE',
   'function': 'FUNCTIONTYPE',
}

tokens = [
    'INT', 'FLOAT', 'PLUS', 'MULTI', 'DIV', 'SUB', 'NAME', 'LPAREN', 'RPAREN', 'COLON', 'COMMA',
    'SEMICOLON', "ARROW", 'EQ', 'OCT', 'HEX', 'GT', 'LT', 'GTE', 'LTE', 'CHAR', 'STRING',
    'EQCOMP', 'NEQ', 'AND', 'OR', 'NOT'
] + list(keywords.values())

t_INT = r'-?[1-9]+[0-9]*'
t_FLOAT = r'-?[0-9]*\.[0-9]+'
t_PLUS = r'\+'
t_MULTI = r'\*'
t_DIV = r'\/'
t_SUB = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r'\:'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_ARROW = r'\-\>'
t_EQ = r'='
t_EQCOMP = r'=='
t_NEQ = r'\!='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_ignore = ' \t'

# Patterns for every token defined by either a function or regular expression
# Regular expressions for legal tokens
t_INT = r'-?[1-9]+[0-9]*'
t_FLOAT = r'-?[0-9]*\.[0-9]+'
t_PLUS = r'\+'
t_MULTI = r'\*'
t_DIV = r'\/'
t_SUB = r'-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r'\:'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_ARROW = r'\-\>'
t_EQ = r'='
t_EQCOMP = r'=='
t_NEQ = r'\!='
t_LT = r'<'
t_GT = r'>'
t_LTE = r'<='
t_GTE = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'\!'

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




