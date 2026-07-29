import cvxpy as cp
import numpy as np

def solve_linear_program():
    """
    Demonstrates a simple Linear Program (LP).
    Problem:
    Minimize: 2x + 3y
    Subject to:
        x + y >= 1
        x >= 0
        y >= 0
    """
    print("--- Solving Linear Program (LP) ---")
    # Define variables
    x = cp.Variable()
    y = cp.Variable()

    # Define constraints
    constraints = [
        x + y >= 1,
        x >= 0,
        y >= 0
    ]

    # Define objective
    objective = cp.Minimize(2 * x + 3 * y)

    # Formulate problem and solve
    prob = cp.Problem(objective, constraints)
    prob.solve()

    print(f"Status: {prob.status}")
    print(f"Optimal value: {prob.value:.4f}")
    print(f"Optimal var x: {x.value:.4f}")
    print(f"Optimal var y: {y.value:.4f}")
    print("\n")


def solve_quadratic_program():
    """
    Demonstrates a simple Quadratic Program (QP) representing 
    Non-Negative Least Squares.
    Problem:
    Minimize: ||Ax - b||_2^2
    Subject to: x >= 0
    """
    print("--- Solving Quadratic Program (QP) ---")
    np.random.seed(1)
    
    # Generate data
    m, n = 15, 10
    A = np.random.randn(m, n)
    b = np.random.randn(m)

    # Define variable
    x = cp.Variable(n)

    # Define constraints (non-negative)
    constraints = [x >= 0]

    # Define objective (sum of squares is a convex quadratic function)
    objective = cp.Minimize(cp.sum_squares(A @ x - b))

    # Formulate problem and solve
    prob = cp.Problem(objective, constraints)
    prob.solve()

    print(f"Status: {prob.status}")
    print(f"Optimal value (Loss): {prob.value:.4f}")
    print(f"Optimal var x (first 3): {x.value[:3]}")
    print("\n")

if __name__ == "__main__":
    solve_linear_program()
    solve_quadratic_program()
