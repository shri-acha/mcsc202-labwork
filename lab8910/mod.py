def euler_method():
    # Problem 8: Euler's method
    f = lambda x, y: x**2 + x
    h = 2.0 / 20  # Step size for 20 sub-intervals
    x = 0
    y = 1
    result = [(x, y)]
    for _ in range(20):
        y = y + h * f(x, y)
        x = x + h
        result.append((x, y))
    return result

def rk2_method():
    # Problem 9: Runge-Kutta 2nd order method
    f = lambda x, y: x**2 + x
    h = 2.0 / 10  # Step size for 10 sub-intervals
    x = 0
    y = 1
    result = [(x, y)]
    for _ in range(10):
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y = y + 0.5 * (k1 + k2)
        x = x + h
        result.append((x, y))
    return result

def finite_difference_method():
    # Problem 10: Finite difference method for BVP
    h = 0.1
    n = 10  # Number of intervals (x0 to x10)
    num_internal = n - 1  # Number of internal points (y1 to y9)

    # Coefficients from the discretized equation
    A = 1 + 32 * h  # Coefficient for y_{i-1}
    B = -2          # Coefficient for y_i
    C = 1 - 32 * h  # Coefficient for y_{i+1}
    RHS = -10 * h**2

    # Initialize tridiagonal matrix components
    a = [0] + [A] * (num_internal - 1)  # Lower diagonal (starts from second equation)
    b = [B] * num_internal               # Main diagonal
    c = [C] * (num_internal - 1) + [0]  # Upper diagonal (last element not used)
    d = [RHS] * num_internal             # Right-hand side

    # Thomas algorithm for tridiagonal system
    # Forward sweep
    cp = [c[0] / b[0]]
    dp = [d[0] / b[0]]
    for i in range(1, num_internal):
        denom = b[i] - a[i] * cp[i-1]
        cp.append(c[i] / denom)
        dp.append((d[i] - a[i] * dp[i-1]) / denom)
    
    # Backward substitution
    y = [0] * num_internal
    y[-1] = dp[-1]
    for i in range(num_internal-2, -1, -1):
        y[i] = dp[i] - cp[i] * y[i+1]
    
    # Combine boundary and internal points
    x_vals = [i * h for i in range(n+1)]
    y_vals = [0] + y + [0]  # y0 = 0, y10 = 0
    return list(zip(x_vals, y_vals))
