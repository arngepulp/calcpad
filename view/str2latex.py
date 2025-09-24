from sympy import Eq, latex
from sympy.parsing.sympy_parser import parse_expr
def str2latex(equation_str):
    if '=' in equation_str:
        left_str, right_str = equation_str.split('=')
        left_expr,right_expr = parse_expr(left_str.strip()), parse_expr(right_str.strip())
        # realized i coulda ran this on a parse eqn_str but thats allrught
        used_symbols = left_expr.free_symbols.union(right_expr.free_symbols)
        equation = Eq(left_expr, right_expr)
        latex_str = latex(equation)
    else: # i know this is literally the worst way to do it but im lazy
        equation_str = equation_str.strip()
        expr = parse_expr(equation_str)
        # realized i coulda ran this on a parse eqn_str but thats allrught
        used_symbols = expr.free_symbols
        latex_str = latex(expr)
    return latex_str