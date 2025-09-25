from model.line import Line
from sympy import symbols, Eq, solve
from sympy.parsing.sympy_parser import parse_expr

class Session:
    def __init__(self):
        self.lines = []
        self.context = {}  # important dictionary storing things!!!! basically why this works
# line building functions
    def rebuild_context(self):
        # this is basically like an update state obj in a numerical simulation
        self.context.clear()
        for line in self.lines:
            if line.var and line.expr:
                self.context[line.var] = line.expr

  
    def add_line(self, raw):
        line = Line(raw)
        self.lines.append(line)
        self.rebuild_context()  # rebuilding context everytime line is edited, greedy eval
        self.eval_all()

    def edit_line(self, raw, idx): # replaces line basically, fake edit but should make more sense in gui
        self.lines[idx] = Line(raw)
        self.rebuild_context()
        return self.eval_all()

    def get_lines(self):
        return self.lines

    def write_lines(self,name,):
        with open(name, 'w') as f:
            for line in self.lines:
                f.write(f"{line.raw_line}\n")

    def read_lines(self, path):
        with open(path) as f:
            line_file = f.read().splitlines()
        
        # Convert each raw line string into a Line object
        self.lines = [Line(raw_line) for raw_line in line_file]

        print(line_file)
        self.rebuild_context()
        self.eval_all()




# line operation objects
    def eval_all(self): # prob gonna make a line specific eval function but idk if needed
        results = {}
        for line in self.lines:
            val = line.eval_line(self.context)
            #if line.var:
            results[line.var] = val
            print(f"> {line.raw_line} = {val}")
        return results
    
    def solve_sym(self,idx,var):
        # setup for symbolic
        line = self.lines[idx] 
        left,right = line.raw_line.split('=',1)
        left,right = left.strip(),right.strip() # prob better way to do this
        left, right = parse_expr(left), parse_expr(right) # idk if this i sneeded
        equation = Eq(left,right)
        varsym = symbols(var)
        # solve
        sol = solve(equation,varsym)
        # back to line ( i rlly should make this a object of line)
        sol = str(sol)
        sol = sol.strip('[]')
        sol = f"{var}="+sol
        self.lines[idx] = Line(sol)
        self.rebuild_context()
    '''
    def diff(self,idx):
        line = self.lines[idx]
        left, right = line.raw_line.split('=')
        dx = diff
    '''
    '''
    def calor(self):
        # somehow implement pycalor??
        y = calor()
        '''