from table import Table
import numpy as np
import math


class FiniteDifferenceTable(Table):

    def __init__(self, x_cols, y_cols, expr, intrvl, step_size, _symbol, expr_mode=True, forward_mode=True):
        self._symbol = _symbol
        self.x_cols = x_cols
        self.y_cols = y_cols
        super().__init__(x_cols.__len__(), x_cols.__len__()+2)
        self.expr = expr
        self.intrvl = intrvl
        self.step_size = step_size
        self.expr_mode = expr_mode
        self.forward_mode = forward_mode
        if (x_cols.__len__() != y_cols.__len__()):
            exit(-1)

    def populate_cols(self):
        if self.forward_mode:
            for idx, x in enumerate(np.arange(int(self.intrvl[0]), int(self.intrvl[1]), self.step_size)):
                self.x_cols[idx] = round(x, 2)
                self.y_cols[idx] = np.round(
                    float(self.expr.subs(self._symbol, x).evalf()), 2)
        else:
            for idx, x in enumerate(np.arange(int(self.intrvl[1]), int(self.intrvl[0]), -self.step_size)):
                self.x_cols[idx] = round(x, 2)
                self.y_cols[idx] = np.round(
                    float(self.expr.subs(self._symbol, x).evalf()), 2)


    def create(self):
        self.label.append('x')
        self.label.append('y')
        if (self.forward_mode):
            for i in range(int(self.ncols)-2):
                self.label.append(f'Δ{i+1}')

            if self.expr_mode:
                self.populate_cols()

            self.table[:, 0] = self.x_cols
            self.table[:, 1] = self.y_cols
            # print(self.table)
            for c_idx in range(2, self.ncols):
                for r_idx in range(self.nrows-(c_idx-1)):
                    self.table[r_idx][c_idx] = round(
                        self.table[r_idx+1][c_idx-1] - self.table[r_idx][c_idx-1], 3)
        else:
            for i in range(int(self.ncols)-2):
                self.label.append(f'∇{i+1}')

            if self.expr_mode:
                self.populate_cols()

            self.table[:, 0] = np.flip(self.x_cols)
            self.table[:, 1] = np.flip(self.y_cols)

            for c_idx in range(2, self.ncols):
                for r_idx in range(self.nrows-(c_idx-1)):
                    self.table[r_idx][c_idx] = -round(
                        self.table[r_idx+1][c_idx-1] - self.table[r_idx][c_idx-1], 3)



    def print(self):
        print('\t'.join(str(label) for label in self.label))
        for row in self.table:
            print('\t'.join(str(rx) for rx in row))
        return
