from model.session import Session
from model.line import Line
from sympy.parsing.latex import parse_latex
from sympy import symbols

class Controller:
    def __init__(self):
        self.s = Session()

    def add_line(self):
        self.s.add_line('')

    def item_changed(self,idx,new_val):
        # this is gonna update the changed value to a line and then eval all
        # new val is str (i tried latek too hard :(()
        if not '#' in new_val:
            if not new_val:
                new_val = ''
            self.s.edit_line(str(new_val),idx)
        else:
            expr, cmd = new_val.split('#')
            expr, cmd = expr.strip(), cmd.strip()
            if 'solve' in cmd:
                cmd = cmd.replace('solve', '').strip()
                self.s.solve_sym(idx,cmd)
            if 'write' in cmd:
                cmd = cmd.replace('write','').strip()
                self.s.write_lines(cmd)
            if 'read' in cmd:
                cmd = cmd.replace('read','').strip()
                self.s.read_lines(cmd)

        results = self.s.eval_all()
        return results, self.s.get_lines()

