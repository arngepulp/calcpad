# line.py
from sympy.parsing.sympy_parser import parse_expr

class Line:
    def __init__(self, raw_line):
        self.raw_line = raw_line.strip()
        self.var = None
        self.expr = None  # symbolic expression

    def eval_line(self, context):
        # only parsed when called
        if '=' in self.raw_line:
            self.var, right = self.raw_line.split('=', 1) # i dont like right variable but idk what else
            self.var = self.var.strip()
            self.expr = parse_expr(right.strip())
        else:
            self.var = None
            self.expr = parse_expr(self.raw_line)

        # allows for symbolic substitution like desmos
        substituted = self.expr.subs(context)
        value = substituted.evalf()

        # symbolic assignment, so if y=2x+3, the value isnt stored, so if x is changed will update!
        if self.var:
            context[self.var] = self.expr
        return value

    def __repr__(self):
        return f"Line('{self.raw_line}')"
