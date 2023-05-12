import ply.yacc as yacc
import parseTree as pt
import globals
from expressionLex import tokens


def p_start_prod(p):
    'function : expr'
    # {saveList($1)};
    globals.trees[globals.task] = p[1]


def p_minus(p):
    '''expr : expr '-' term'''
    # {$$ = doOp2($1, $3, " - ");};
    p[0] = pt.Function(2, p[1], p[3], "-", None)


def p_plus(p):
    '''expr : expr '+' term'''
    # {$$ = doOp2($1, $3, " + ");};
    p[0] = pt.Function(2, p[1], p[3], "+", None)


def p_term_to_expr(p):
    '''expr : term'''
    # {$$ = $1;};
    p[0] = p[1]


def p_times(p):
    '''term : term '*' factor'''
    # {$$ = doOp2($1, $3, " * ");};
    p[0] = pt.Function(2, p[1], p[3], "*", None)


def p_divide(p):
    '''term	: term '/' factor'''
    # {$$ = doOp2($1, $3, " / ");};
    p[0] = pt.Function(2, p[1], p[3], "/", None)


def p_mod(p):
    '''term : term '%' factor'''
    # {$$ = doOp2($1, $3, " % ");};
    p[0] = pt.Function(2, p[1], p[3], "%", None)


def p_factor_to_term(p):
    '''term : factor'''
    # {$$ = $1;};
    p[0] = p[1]


def p_do_pow(p):
    '''factor :	num '^' factor'''
    # {$$ = doOp2($1, $3, " ^ ");};
    p[0] = pt.Function(2, p[1], p[3], "^", None)


def p_num_to_factor(p):
    '''factor :	num'''
    # {$$ = $1;};
    p[0] = p[1]


def p_do_sin(p):
    '''num : SIN1 '(' expr ')'
           | SIN2 '(' expr ')'
           | SIN3 '(' expr ')' '''
    # {$$ = doOp1($3, "Sin");};
    p[0] = pt.Function(1, p[3], None, "Sin", None)


def p_do_cos(p):
    '''num : COS1 '(' expr ')'
           | COS2 '(' expr ')'
           | COS3 '(' expr ')' '''
    # {$$ = doOp1($3, "Cos");};
    p[0] = pt.Function(1, p[3], None, "Cos", None)


def p_do_tan(p):
    '''num : TAN1 '(' expr ')'
           | TAN2 '(' expr ')'
           | TAN3 '(' expr ')' '''
    # {$$ = doOp1($3, "Tan");};
    p[0] = pt.Function(1, p[3], None, "Tan", None)


def p_do_sqrt(p):
    '''num : SQRT1 '(' expr ')'
           | SQRT2 '(' expr ')'
           | SQRT3 '(' expr ')' '''
    # {$$ = doOp1($3, "Rot");};
    p[0] = pt.Function(1, p[3], None, "Rot", None)


def p_parens(p):
    '''num : '(' expr ')' '''
    # {$$ = $2}
    p[0] = p[2]


def p_neg(p):
    '''num : '-' num'''
    # {$$ = doOp1($2, "Neg");};
    p[0] = pt.Function(1, p[1], None, "Neg", None)


def p_make_int(p):
    '''num : INT'''
    # {$$ = useInt(atoi(yytext));};
    p[0] = pt.Function(2, None, None, None, pt.Data(p[1], 1))


def p_make_double(p):
    '''num : FLOAT'''
    # {$$ = useDouble(atof(yytext));};
    p[0] = pt.Function(2, None, None, None, pt.Data(p[1], 1))


def p_make_id(p):
    '''num : id'''
    # {$$ = useId($1)};
    p[0] = pt.Function(2, None, None, None, p[1])


def p_name_to_id(p):
    '''id : NAME'''
    if p[1] == "$t":
        # this is a reference to the timestep value
        p[0] = pt.Data(p[1], 0)
    elif not 0 <= int(p[1][2:]) < globals.numTasks:
        globals.parserError = True
        globals.errorMessage = "Illegal task reference {}".format(p[1])
    else:
        if p[1] == "$t{}".format(globals.task):
            # This is a self-referential task, so we will not add a cycle
            pass
        else:
            # Add this function as a child of the task it references (duplicates are ignored)
            globals.graph.find_node(p[1]).add_child(globals.node)
        # add a data node to the tree with the value of the named task
        p[0] = pt.Data(p[1], 0)


# Rule for syntax errors
def p_error(p):
    globals.parserError = True
    if p is None:
        globals.errorMessage = "Unexpectedly reached the end of expression."
    elif p.type is None:
        globals.errorMessage = "Illegal character {}".format(p.value[0])
    else:
        globals.errorMessage = "Syntax error at {}".format(p.value)
    print("Syntax error in input!\n" + globals.errorMessage)


parser = yacc.yacc()
