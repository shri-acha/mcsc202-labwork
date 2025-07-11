import numpy as np
from sympy import symbols, parse_expr
from finite_difference import FiniteDifferenceTable
import math


class Data:
    def __init__(self, x, y, step):

        # Data (x,y) stored in a np array
        self.x = x
        self.y = y
        self.step = step
        self.expr = None

        self.fsdt = FiniteDifferenceTable(
            x,
            y,
            None,
            (-1, 1),
            1, None, expr_mode=False,forward_mode=False)

        self.fsdt.create()  # Load the finite_difference table

    def finterpolate(self):
        expr_str = ''
        # Starting out after leaving the leading y column
        for idx, i in enumerate(range(1, self.fsdt.nrows+2)):
            expr_str += f"({self.fsdt.table[0, i]} * ( {self.coefficient('x', idx-1)} ) ) / ({self.step}**{idx} * {math.factorial(idx)} ) "
            if i != self.fsdt.nrows + 2 - 1:
                expr_str += "+"
        self.expr = parse_expr(expr_str)
        return

    def binterpolate(self):
        expr_str = ''
        # Starting out after leaving the leading y column
        for idx, i in enumerate(range(1, self.fsdt.nrows+2)):
            expr_str += f"({self.fsdt.table[0, i]} * ( {self.coefficient('x', idx-1)} ) ) / ({self.step}**{idx} * {math.factorial(idx)} ) "
            if i != self.fsdt.nrows + 2 - 1:
                expr_str += "+"
        self.expr = parse_expr(expr_str)
        return

    def coefficient(self, x, data_idx):
        if (data_idx < 0):
            return '1'
        return f'({x}-{self.fsdt.table[data_idx, 0]})'+'*' + f'{self.coefficient(x, data_idx-1)}'
