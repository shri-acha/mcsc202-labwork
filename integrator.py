from numpy import arange


class Integrator:
    def __init__(self, function, interval, parts,symbol):

        self.function = function
        self.interval = interval
        self.parts = parts

        self.solution = float()
        self.step = (interval[1] - interval[0])/parts
        self.symbol = symbol

        self.x_arr = arange(
            self.interval[0], self.interval[1], self.step).tolist()
        self.y_arr = list(
            map(lambda x: self.function.subs(self.symbol, x).evalf(), self.x_arr))


    def execute():
        pass
