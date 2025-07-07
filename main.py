from bisection import Bisection
from newton_raphson import NewtonRaphson
from finite_difference import FiniteDifferenceTable
import numpy as np
from sympy import symbols, sin, solve, exp


def main():
    x = symbols('x')
    expr = exp(x) 
    # solution = solve(expr, x)
    # bsc = Bisection((-3, -1), expr, x, 0.01)
    # print('[DEBUG]  x     df    f\n')
    # nwtn = NewtonRaphson(expr, x, 0.0001, 3.0)

    fsdt = FiniteDifferenceTable(np.zeros(20), np.zeros(20), expr, (-1, 1), 0.1,x)
    fsdt.create()
    fsdt.print()


if __name__ == "__main__":
    main()
