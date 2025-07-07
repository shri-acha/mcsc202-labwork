from approximation import Approximation
import time


class NewtonRaphson(Approximation):
    def __init__(self, exprs, _symbol, tolerance, init_guess):
        super().__init__(exprs, _symbol, tolerance)
        self.init_guess = init_guess

    def approximate(self):

        d_function = self.function.diff(self._symbol)

        x0 = self.init_guess
        df0 = d_function.subs(self._symbol, x0).evalf()
        f0 = self.function.subs(self._symbol, x0).evalf()

        print(f'[DEBUG] {x0} {df0} {f0}\n')

        self.root = x0 - f0/df0

        if (self.root):
            f1 = self.function.subs(self._symbol, self.root).evalf()
            if abs(f1) <= self.tolerance:
                return self.root
            if (f1 == 0):
                return self.root

        self.init_guess = self.root
        return self.approximate()
