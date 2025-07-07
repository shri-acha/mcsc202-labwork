import numpy as np


class Table():
    def __init__(self, nrows, ncols):
        self.label = list()
        self.nrows = nrows
        self.ncols = ncols
        self.table = np.zeros((nrows, ncols))
        pass

    def print(self):
        pass
