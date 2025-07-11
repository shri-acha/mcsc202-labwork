from bisection import Bisection
from newton_raphson import NewtonRaphson
from newtons_interpolation import Data
from finite_difference import FiniteDifferenceTable
import numpy as np
from sympy import symbols, sin, solve, exp,simplify


def main():
    x = symbols('x')
    h = symbols('h')
    expr = exp(x) 
    # solution = solve(expr, x)
    # bsc = Bisection((-3, -1), expr, x, 0.01)
    # print('[DEBUG]  x     df    f\n')
    # nwtn = NewtonRaphson(expr, x, 0.0001, 3.0)

    # fsdt = FiniteDifferenceTable(np.zeros(20), np.zeros(20), expr, (-1, 1), 0.1,x)
    # fsdt.create()
    # fsdt.print()
    handler = Data(np.array([0,1,2,3,4,5]),np.array([0,0.165,0.232,0.371,0.468,0.502]),step=1)

    # handler.finterpolate()
    # print(simplify(handler.expr).subs(x,3))
    handler.binterpolate()
    print(simplify(handler.expr).subs(x,5))
    handler.fsdt.print()


if __name__ == "__main__":
    main()
