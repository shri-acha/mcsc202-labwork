from integrator import Integrator


class SimpsonsThird(Integrator):
    def __init__(self, function, interval, parts, symbol):
        super().__init__(function, interval, parts, symbol)

    def integrate(self):
        print(f'[DEBUG]\nfunction:\t{self.function}\tstep:'
              f'{self.step}\tparts:{self.parts}')
        for idx, y in enumerate(self.y_arr):
            print(f'solution:\t{((self.step/3)*(self.solution)).evalf()}\titeration:{idx}')
            if idx == 0 or idx == self.parts - 1:
                self.solution += y
            else:
                if idx % 2 == 0:
                    self.solution += 2*y
                if idx % 2 != 0:
                    self.solution += 4*y
        self.solution *= self.step/3
        return self.solution
