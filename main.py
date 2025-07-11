
from lab1.bisection import Bisection
from lab2.newton_raphson import NewtonRaphson
from lab3.finite_difference import FiniteDifferenceTable
from lab4.newtons_interpolation import Data
from lab5.lagrange_interpolation import Data

import numpy as np
from sympy import symbols, sin, solve, exp, simplify, parse_expr


def main():
    x = symbols('x')
    h = symbols('h')
    expr_bis = x**2 - sin(x)
    expr_new = exp(x) - 4*x
    expr_fsdt = exp(x)

    # BISECTION AND NEWTON RAPHSON METHOD ON SOLVING
    # UNCOMMENT THIS BLOCK

    # bsc = Bisection(expr_bis,x, 0.001,(0.5, 1))
    # print('[DEBUG]  x     df    f\n')
    # nwtn = NewtonRaphson(expr_new, x, 0.0001, 3.0)
    # print(f'[APPROXIMATE]:{bsc.approximate()}')
    # print(f'[APPROXIMATE]:{nwtn.approximate()}')

    # FINITE STATE DIFFERENCE TABLE
    # UNCOMMENT THIS BLOCK
    # fsdt = FiniteDifferenceTable(np.zeros(20), np.zeros(20), expr_fsdt, (-1, 1), 0.1,x)
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
