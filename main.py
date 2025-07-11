from bisection import Bisection
from newton_raphson import NewtonRaphson
from newtons_interpolation import Data
from finite_difference import FiniteDifferenceTable
import numpy as np
from sympy import symbols, sin, solve, exp, simplify, parse_expr
from lagrange_interpolation import Data


def main():
    x = symbols('x')
    h = symbols('h')
    # expr = exp(x)
    # solution = solve(expr, x)

    # BISECTION AND NEWTON RAPHSON METHOD ON SOLVING
    # UNCOMMENT THIS BLOCK
    # bsc = Bisection((-3, -1), expr, x, 0.01)
    # print('[DEBUG]  x     df    f\n')
    # nwtn = NewtonRaphson(expr, x, 0.0001, 3.0)

    # FINITE STATE DIFFERENCE TABLE
    # UNCOMMENT THIS BLOCK
    # fsdt = FiniteDifferenceTable(np.zeros(20), np.zeros(20), expr, (-1, 1), 0.1,x)
    # fsdt.create()
    # fsdt.print()

    # NEWTON'S FORWARD AND BACKWARD INTERPOLATION
    # UNCOMMENT THIS BLOCK
    #
    # handler = Data(np.array([0,1,2,3,4,5]),np.array([0,0.165,0.232,0.371,0.468,0.502]),step=1)
    #
    # # handler.finterpolate()
    # # print(simplify(handler.expr).subs(x,3))
    # handler.binterpolate()
    # print(simplify(handler.expr).subs(x,5))
    # handler.fsdt.print()

    # LAGRANGE'S INTERPOLATION
    # UNCOMMENT THIS BLOCK
    # handler_ = Data(np.array([0, 1, 3, 4, 5]),
    #                 np.array([0, 1, 81, 256, 625]))

    # print(handler_.interpolate_().subs(x, 2))


if __name__ == "__main__":
    main()
