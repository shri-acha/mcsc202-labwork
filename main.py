from bisection import Bisection
from newton_raphson import NewtonRaphson
from sympy import symbols, sin, solve, exp


def main():
    x = symbols('x')
    expr = exp(x) - 4*x
    # solution = solve(expr, x)
    # bsc = Bisection((-3, -1), expr, x, 0.01)
    print('[DEBUG]  x     df    f\n')
    nwtn = NewtonRaphson(expr, x, 0.0001, 3.0)
    print(f'Approximate:{nwtn.approximate()}\t')


if __name__ == "__main__":
    main()
