# line.py
from sympy.parsing.sympy_parser import parse_expr
from pyCalor import thermo as th

class Line:
    def __init__(self, raw_line):
        self.raw_line = raw_line.strip()
        self.var = None
        self.expr = None  # symbolic expression

    def eval_line(self, context):
        if not self.raw_line:
            self.expr = None
            return None

        if '=' in self.raw_line:
            lhs, rhs = self.raw_line.split('=', 1)
            self.var = lhs.strip()
            expr_str = rhs.strip()
        else:
            self.var = None
            expr_str = self.raw_line.strip()

        # Heuristic: if expr_str refers to state or uses “.” (attribute) or “th.state”, use eval
        use_eval = False
        if "th.state" in expr_str or "." in expr_str:
            # But be careful: sympy expressions may also use ".", e.g. “x**2”. However “.” usually means attribute access
            use_eval = True

        if use_eval:
            # Build a safe environment
            local_env = {}
            # allow access to pyCalor, and existing variables in context
            local_env["th"] = th
            # Also inject any Python values from context (only ones that are not sympy Expr objects)
            for k, v in context.items():
                # If v is a sympy expression, it may not function well in pure Python eval
                # We could convert to float if numeric, or leave as is
                local_env[k] = v

            try:
                value = eval(expr_str, {"__builtins__": {}}, local_env)
                self.expr = value
            except Exception as e:
                print(f"Error evaluating Python line `{expr_str}`: {e}")
                self.expr = None
                value = None
        else:
            # Use sympy
            try:
                self.expr = parse_expr(expr_str)
                substituted = self.expr.subs(context)
                value = substituted.evalf()
            except Exception as e:
                print(f"Error parsing sympy line `{expr_str}`: {e}")
                self.expr = None
                value = None

        if self.var is not None:
            context[self.var] = self.expr

        return value

    def __repr__(self):
        return f"Line('{self.raw_line}')"
