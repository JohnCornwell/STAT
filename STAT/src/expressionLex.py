import ply.lex as lex

# Lexer construction from the PLY documentation:
# When building the master regular expression, rules are added in the following order:
# All tokens defined by functions are added in the same order as they appear in the lexer file.
# Tokens defined by strings are added next by sorting them in order of decreasing regular expression
# length (longer expressions are added first).

reserved = {
    'sin': 'SIN1',
    'Sin': 'SIN2',
    'SIN': 'SIN3',
    'cos': 'COS1',
    'Cos': 'COS2',
    'COS': 'COS3',
    'tan': 'TAN1',
    'Tan': 'TAN2',
    'TAN': 'TAN3',
    'sqrt': 'SQRT1',
    'Sqrt': 'SQRT2',
    'SQRT': 'SQRT3'
}

tokens = ['NAME', 'INT', 'FLOAT'] + list(reserved.values())

literals = ['^', '+', '-', '*', '/', '%', '(', ')']

# Definitions of tokens and actions to take
t_NAME = r'\$t[0-9]*'

def t_FLOAT(t):
    r'\d+\.\d+'
    # This needs to be above int definition due to how rules are added by ply
    # All tokens defined by functions are added in the same order as they appear in the lexer file.
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Handles tokens from the reserved list
def t_ID(t):
    r'[a-zA-Z][a-zA-Z]*'
    if t.value in reserved:
        t.type = reserved[t.value]
        return t
    else:
        # this word is not in the reserved list, so it is an illegal
        # token that will be handled by the parser
        return t


t_ignore = " \t\n\r"


def t_eof(t):
    more = None
    if more:
        t.lexer.input(more + '\n')
        return t.lexer.token()
    else:
        return None


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.type = None
    t.lexer.skip(1)
    return t


# Build the lexer object
lexer = lex.lex()
