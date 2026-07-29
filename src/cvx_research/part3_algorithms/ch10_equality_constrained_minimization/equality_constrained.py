import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x[0]**4 + x[1]**4

def grad_f(x):
    return np.array([4 * x[0]**3, 4 * x[1]**3])

def hessian_f(x):
    return np.array([[12 * x[0]**2, 0],
                     [0, 12 * x[1]**2]])

def backtracking_line_search(x, dx, A, alpha=0.1, beta=0.7):
    t = 1.0
    val_x = f(x)
    grad_x = grad_f(x)
    
    while f(x + t * dx) > val_x + alpha * t * grad_x.T @ dx:
        t *= beta
    return t

def equality_constrained_newton(x0, A, b, tol=1e-5, max_iters=20):
    """
    Feasible start Newton's method for equality constrained problems.
    Minimizes f(x) subject to Ax = b.
    Requires Ax0 = b.
    """
    x = x0.copy()
    path = [x.copy()]
    
    p = A.shape[0]
    n = x.shape[0]
    
    for _ in range(max_iters):
        g = grad_f(x)
        H = hessian_f(x)
        
        # Form the KKT matrix
        KKT = np.block([
            [H, A.T],
            [A, np.zeros((p, p))]
        ])
        
        # Right hand side
        rhs = np.concatenate([-g, np.zeros(p)])
        
        # Solve the KKT system
        sol = np.linalg.solve(KKT, rhs)
        dx = sol[:n]
        
        # Newton decrement
        lambda_sq = dx.T @ H @ dx
        if lambda_sq / 2.0 <= tol:
            break
            
        t = backtracking_line_search(x, dx, A)
        x = x + t * dx
        path.append(x.copy())
        
    return np.array(path)

def demonstrate_algorithm():
    # Constraint: x1 + 2*x2 = 2
    A = np.array([[1.0, 2.0]])
    b = np.array([2.0])
    
    # Feasible starting point (must satisfy Ax = b)
    x0 = np.array([4.0, -1.0])
    
    path = equality_constrained_newton(x0, A, b)
    
    # Plotting
    X1, X2 = np.meshgrid(np.linspace(-2, 5, 100), np.linspace(-2, 3, 100))
    Z = X1**4 + X2**4
    
    plt.figure(figsize=(10, 8))
    plt.contour(X1, X2, Z, levels=np.logspace(-1, 3, 20), cmap='viridis', alpha=0.5)
    
    # Plot the constraint line x1 + 2*x2 = 2 => x2 = 1 - 0.5*x1
    x1_line = np.linspace(-2, 5, 100)
    x2_line = 1.0 - 0.5 * x1_line
    plt.plot(x1_line, x2_line, 'k-', lw=2, label='Constraint $x_1 + 2x_2 = 2$')
    
    # Plot path
    plt.plot(path[:, 0], path[:, 1], 'ro-', markersize=6, lw=2, label="Newton's Method Path")
    
    # Optimum
    plt.plot(path[-1, 0], path[-1, 1], 'b*', markersize=15, label='Optimum')
    
    plt.title("Equality Constrained Newton's Method")
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("equality_constrained.png")
    print(f"Optimization complete in {len(path)-1} iterations. Plot saved as equality_constrained.png")
    print(f"Optimal x: {path[-1]}")

if __name__ == "__main__":
    demonstrate_algorithm()
