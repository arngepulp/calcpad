from line import Line

class Session:
    def __init__(self):
        self.lines = []
        self.context = {}  # important dictionary storing things!!!! basically why this works

    def rebuild_context(self):
        # this is basically like an update state obj in a numerical simulation
        self.context.clear()
        for line in self.lines:
            if line.var and line.expr:
                self.context[line.var] = line.expr

    def eval_all(self): # prob gonna make a line specific eval function but idk if needed
        results = {}
        for line in self.lines:
            val = line.eval_line(self.context)
            if line.var:
                results[line.var] = val
            print(f"> {line.raw_line} = {val}")
        return results

    def add_line(self, raw):
        line = Line(raw)
        self.lines.append(line)
        self.rebuild_context()  # rebuilding context everytime line is edited, greedy eval
        self.eval_all()

    def edit_line(self, raw, idx): # replaces line basically, fake edit but should make more sense in gui
        self.lines[idx] = Line(raw)
        self.rebuild_context()
        self.eval_all()
