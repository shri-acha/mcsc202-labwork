from newtons_interpolation import FiniteDifferenceTable
from sympy import symbols,simplify,parse_expr


class Data:
    def __init__(self, x_arr, y_arr):

        # Data (x,y) stored in a np array
        self.symbol_ = symbols('x')
        self.x_arr = x_arr
        self.y_arr = y_arr
        self.expr = None

    def interpolate_(self):
        expr_str = ""
        numerator = ""
        denomenator = ""

        for y in range(0,len(self.y_arr)):
            numerator = ""
            denomenator = ""
            for x in range(0,len(self.x_arr)):
                if ( y == x ):
                    continue
                numerator += f"(x-{self.x_arr[x]}) "
                denomenator += f"({self.x_arr[y]}-{self.x_arr[x]}) "
            numerator = numerator.strip().split(' ')
            numerator = "*".join(numerator)
            denomenator= denomenator.strip().split(' ')
            denomenator = "*".join(denomenator)
            numerator += f"*({self.y_arr[y]})"
            
            expr_str += f"({numerator})/({denomenator}) "

        arr_buf = expr_str.strip().split(' ')
        
        expr_str = '+'.join(arr_buf)
        return parse_expr(expr_str)
