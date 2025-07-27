import numpy as np

def solve_bvp_finite_difference():
    """
    Solves the BVP y'' - 64y' + 10 = 0 using the finite difference method.
    Boundary Conditions: y(0) = 0, y(1) = 0
    Step Size (h): 0.1
    """
    print("## 10. Solving Boundary Value Problem with Finite Difference Method")

    # --- Setup ---
    h = 0.1  # Step size
    x_start, x_end = 0, 1
    y_start, y_end = 0, 0

    # Number of internal grid points
    N = int((x_end - x_start) / h) - 1
    
    # Create the matrix A and vector b for the system Ay = b
    A = np.zeros((N, N))
    b = np.full(N, -10 * h**2)

    # --- Finite Difference Equation ---
    # y_i-1 * (1 + 32h) - 2*y_i + y_i+1 * (1 - 32h) = -10 * h^2
    # With h = 0.1: 4.2*y_i-1 - 2*y_i - 2.2*y_i+1 = -0.1

    # --- Populate Matrix A ---
    # The coefficients for y_{i-1}, y_i, and y_{i+1}
    c_prev = 1 + 32 * h  # 4.2
    c_curr = -2
    c_next = 1 - 32 * h  # -2.2

    for i in range(N):
        # Main diagonal (coefficient of y_i)
        A[i, i] = c_curr
        # Upper diagonal (coefficient of y_{i+1})
        if i < N - 1:
            A[i, i + 1] = c_next
        # Lower diagonal (coefficient of y_{i-1})
        if i > 0:
            A[i, i - 1] = c_prev
    
    # Adjust for boundary conditions (both are 0, so no change to b)
    # If y_start or y_end were non-zero, they would be adjusted here.
    # b[0] -= c_prev * y_start
    # b[N-1] -= c_next * y_end

    # --- Solve the System ---
    try:
        y_internal = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        print("Error: The matrix is singular and the system cannot be solved.")
        return

    # Combine boundary points with the internal solution
    y_solution = np.concatenate(([y_start], y_internal, [y_end]))
    x_points = np.arange(x_start, x_end + h, h)

    # --- Print Results ---
    print("The system of equations is derived from: 4.2*y_{i-1} - 2*y_i - 2.2*y_{i+1} = -0.1")
    print("\nSolution for y(x) at each step:")
    for x, y in zip(x_points, y_solution):
        print(f"  y({x:.1f}) = {y:.6f}")
    print("-" * 40)


def fit_linear_least_squares():
    """
    Fits a straight line y = a0 + a1*x to the given data using the least square method.
    Estimates y at x = 2.5.
    """
    print("## 11. Linear Least Square Fit")

    # --- Data ---
    x_data = np.array([1, 2, 3, 4, 5, 6])
    y_data = np.array([2.4, 3.1, 3.5, 4.2, 5.0, 6.0])
    x_estimate = 2.5

    # --- Calculations for Normal Equations ---
    n = len(x_data)
    sum_x = np.sum(x_data)
    sum_y = np.sum(y_data)
    sum_x2 = np.sum(x_data**2)
    sum_xy = np.sum(x_data * y_data)

    # --- Setup and Solve the System Aa = B ---
    # n*a0 + sum(x)*a1 = sum(y)
    # sum(x)*a0 + sum(x^2)*a1 = sum(xy)
    A = np.array([[n, sum_x], [sum_x, sum_x2]])
    B = np.array([sum_y, sum_xy])

    try:
        # coeffs[0] is a0, coeffs[1] is a1
        coeffs = np.linalg.solve(A, B)
        a0, a1 = coeffs[0], coeffs[1]
    except np.linalg.LinAlgError:
        print("Error: The matrix is singular and the system cannot be solved.")
        return

    # --- Estimate Value ---
    y_estimate = a0 + a1 * x_estimate

    # --- Print Results ---
    print(f"The fitted straight line is: y = {a0:.4f} + {a1:.4f}x")
    print(f"\nEstimated value of y at x = {x_estimate} is: {y_estimate:.4f}")
    print("-" * 40)


def fit_exponential_least_squares():
    """
    Fits a curve y = a*e^(bx) to the given data using the least square method.
    Estimates y at x = 9.
    """
    print("## 12. Exponential Least Square Fit")
    
    # --- Data ---
    x_data = np.array([2, 4, 6, 8, 10])
    y_data = np.array([4.077, 11.084, 30.128, 81.897, 222.62])
    x_estimate = 9

    # --- Linearize the Model ---
    # y = a*e^(bx)  =>  ln(y) = ln(a) + b*x
    # Let Y = ln(y), A0 = ln(a), A1 = b.  So, Y = A0 + A1*x
    Y_data = np.log(y_data)

    # --- Calculations for Normal Equations (on linearized data) ---
    n = len(x_data)
    sum_x = np.sum(x_data)
    sum_Y = np.sum(Y_data)
    sum_x2 = np.sum(x_data**2)
    sum_xY = np.sum(x_data * Y_data)

    # --- Setup and Solve the System Aa = B ---
    A = np.array([[n, sum_x], [sum_x, sum_x2]])
    B = np.array([sum_Y, sum_xY])

    try:
        # A_coeffs[0] is A0, A_coeffs[1] is A1
        A_coeffs = np.linalg.solve(A, B)
        A0, A1 = A_coeffs[0], A_coeffs[1]
    except np.linalg.LinAlgError:
        print("Error: The matrix is singular and the system cannot be solved.")
        return

    # --- Convert back to original parameters a and b ---
    b = A1
    a = np.exp(A0)

    # --- Estimate Value ---
    y_estimate = a * np.exp(b * x_estimate)

    # --- Print Results ---
    print(f"The fitted curve is: y = {a:.4f} * e^({b:.4f}x)")
    print(f"\nEstimated value of y at x = {x_estimate} is: {y_estimate:.4f}")
    print("-" * 40)


if __name__ == "__main__":
    solve_bvp_finite_difference()
    fit_linear_least_squares()
    fit_exponential_least_squares()
