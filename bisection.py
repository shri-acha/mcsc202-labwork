from approximation import Approximation


class Bisection(Approximation):
    def __init__(self, exprs, _symbol, tolerance, init_int):
        self.function = exprs
        self._symbol = _symbol
        self.tolerance = tolerance
        self.init_int = init_int
        self.root = None

    def approximate(self):
        tolerance = self.tolerance
        if self.root:
            y0 = self.function.subs(self._symbol, self.root)
            if (tolerance >= abs(y0)):
                # print(f'{tolerance} {y0}')
                return self.root

        fa = self.function.subs(self._symbol, self.init_int[0])
        fb = self.function.subs(self._symbol, self.init_int[1])
        a = self.init_int[0]
        b = self.init_int[1]

        # print(f'[DEBUG] {self.init_int}')
        # check if the interval contains the root
        if ((fa*fb) < 0):

            # Substituting x with (a+b)/2
            self.root = (a+b)/2

            y0 = self.function.subs(self._symbol, self.root)
            print(f'[DEBUG] f(a)*root:{y0*fa < 0}\tf(b)*root:{y0*fb < 0}')
            # root is between a and x0
            if (y0*fa < 0):
                self.init_int = (a, self.root)
                return self.approximate()

            # root is between x0 and b
            elif (y0*fb < 0):
                self.init_int = (self.root, b)
                return self.approximate()
            # root is x0
            else:
                return self.root

            # If root is in the boundary
        elif (fa*fb == 0):
            if (fa == 0):
                self.root = a
                return self.root
            else:
                self.root = b
                return self.root
