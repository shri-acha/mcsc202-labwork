from bisection import Bisection
from sympy import symbols, sin, solve, exp


def main():
    x = symbols('x')
    expr = exp(x) - x - 2
    # solution = solve(expr, x)
    bsc = Bisection((-3, -1), expr, x, 0.01)
    print(f'Approximate:{bsc.approximate()}\t')


if __name__ == "__main__":
    main()
