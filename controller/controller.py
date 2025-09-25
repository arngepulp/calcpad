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
        # convert the str to sympy usuable
        # edit line
        s.edit_line
        # update gui

