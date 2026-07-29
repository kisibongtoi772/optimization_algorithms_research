import cvxpy as cp
import numpy as np

def demonstrate_strong_duality():
    """
    Demonstrates Strong Duality by solving both the Primal
    and the Dual of a Linear Program.
    
    Primal (Standard Form LP):
    Minimize: c^T x
    Subject to: Ax = b, x >= 0
    
    Dual LP:
    Maximize: -b^T nu
    Subject to: -A^T nu + c >= 0
    """
    np.random.seed(42)
    m, n = 5, 10
    
    # Generate random data. Ensure A, b, c give a feasible bounded LP
    A = np.random.randn(m, n)
    # create a feasible x to ensure A x = b is possible for x >= 0
    x0 = np.random.rand(n) 
    b = A @ x0
    c = np.random.rand(n) # positive cost to ensure boundedness

    print("--- 1. Solving Primal Problem ---")
    x = cp.Variable(n)
    primal_constraints = [A @ x == b, x >= 0]
    primal_prob = cp.Problem(cp.Minimize(c.T @ x), primal_constraints)
    primal_prob.solve()
    
    p_star = primal_prob.value
    print(f"Primal Optimal Value (p*): {p_star:.4f}")

    print("\n--- 2. Solving Dual Problem ---")
    # For constraints Ax = b, dual variable is nu (free)
    # For constraints x >= 0 (-x <= 0), dual variable is lambda >= 0
    # Following standard LP duality derived from the Lagrangian
    nu = cp.Variable(m)
    dual_constraints = [-A.T @ nu + c >= 0]
    dual_prob = cp.Problem(cp.Maximize(-b.T @ nu), dual_constraints)
    dual_prob.solve()
    
    d_star = dual_prob.value
    print(f"Dual Optimal Value (d*): {d_star:.4f}")
    
    print("\n--- 3. Verifying Strong Duality ---")
    gap = abs(p_star - d_star)
    print(f"Duality Gap |p* - d*| = {gap:.4e}")
    if gap < 1e-5:
        print("Strong duality holds!")
        
    print("\n--- 4. Extracting Dual Variables (Shadow Prices) from Primal ---")
    # cvxpy automatically stores the dual variables in the constraints after solve
    nu_star_extracted = primal_constraints[0].dual_value
    print(f"Dual variable (nu) from primal constraint: {nu_star_extracted}")
    print(f"Dual variable (nu) from dual solver: {nu.value}")
    
if __name__ == "__main__":
    demonstrate_strong_duality()
