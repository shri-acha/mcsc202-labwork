from integrator import Integrator
from numpy import arange


class Trapezoidal_Integration(Integrator):
    def __init__(self, function, interval, parts, symbol):
        super().__init__(function, interval, parts,symbol)

    def integrate(self):

        for idx, i in enumerate(self.y_arr):
            if ((idx == 0) or idx == (self.parts-1)):
                self.solution += i.evalf()
            else:
                self.solution += 2*i.evalf()
        self.solution = (self.step/2)*self.solution.evalf()

        print(f'Solution:\t{self.solution.evalf()}\n{self.x_arr}\n{self.y_arr}')
