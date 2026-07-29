import numpy as np
import matplotlib.pyplot as plt

def barrier_objective(x, c, A, b, t):
    # - sum(log(b - Ax))
    d = b - A @ x
    if np.any(d <= 0):
        return np.inf
    return t * c.T @ x - np.sum(np.log(d))

def barrier_gradient(x, c, A, b, t):
    d = b - A @ x
    return t * c + A.T @ (1.0 / d)

def barrier_hessian(x, A, b):
    d = b - A @ x
    return A.T @ np.diag(1.0 / d**2) @ A

def backtracking_line_search(x, dx, c, A, b, t, alpha=0.1, beta=0.7):
    step = 1.0
    val_x = barrier_objective(x, c, A, b, t)
    grad_x = barrier_gradient(x, c, A, b, t)
    
    # Must stay strictly feasible
    while np.any(b - A @ (x + step * dx) <= 0):
        step *= beta
        
    while barrier_objective(x + step * dx, c, A, b, t) > val_x + alpha * step * grad_x.T @ dx:
        step *= beta
    return step

def centering_step(x0, c, A, b, t, tol=1e-5):
    x = x0.copy()
    for _ in range(50):
        g = barrier_gradient(x, c, A, b, t)
        H = barrier_hessian(x, A, b)
        dx = -np.linalg.solve(H, g)
        
        lambda_sq = dx.T @ H @ dx
        if lambda_sq / 2.0 <= tol:
            break
            
        step = backtracking_line_search(x, dx, c, A, b, t)
        x = x + step * dx
    return x

def barrier_method(x0, c, A, b, t0=1.0, mu=10, tol=1e-3):
    m = len(b)
    t = t0
    x = x0.copy()
    
    central_path = [x.copy()]
    
    while m / t >= tol:
        x = centering_step(x, c, A, b, t)
        central_path.append(x.copy())
        t *= mu
        
    return np.array(central_path)

def demonstrate_barrier_method():
    # Linear Program: minimize c^T x subject to Ax <= b
    c = np.array([-1.0, -1.0])
    
    # Feasible region: a simple polygon
    A = np.array([
        [ 1.0,  0.0],
        [ 0.0,  1.0],
        [-1.0,  0.0],
        [ 0.0, -1.0],
        [ 1.0,  1.0]
    ])
    b = np.array([2.0, 2.0, 0.0, 0.0, 3.0])
    
    # Strictly feasible starting point
    x0 = np.array([0.5, 0.5])
    
    path = barrier_method(x0, c, A, b, t0=1.0, mu=2.0)
    
    plt.figure(figsize=(8, 8))
    
    # Plot feasible region constraints
    x_grid = np.linspace(-0.5, 2.5, 400)
    y_grid = np.linspace(-0.5, 2.5, 400)
    X, Y = np.meshgrid(x_grid, y_grid)
    
    # Check if inside all constraints
    feasible = (X <= 2) & (Y <= 2) & (-X <= 0) & (-Y <= 0) & (X + Y <= 3)
    plt.contourf(X, Y, feasible, levels=[0.5, 1.5], colors=['lightblue'], alpha=0.5)
    
    # Plot contour of objective c^T x
    Z = c[0]*X + c[1]*Y
    plt.contour(X, Y, Z, levels=10, cmap='gray', alpha=0.3)
    
    # Plot central path
    plt.plot(path[:, 0], path[:, 1], 'ro-', lw=2, markersize=5, label='Central Path')
    plt.plot(path[0, 0], path[0, 1], 'ko', label='Start')
    plt.plot(path[-1, 0], path[-1, 1], 'b*', markersize=15, label='Optimum')
    
    plt.title("Barrier Method Central Path for LP")
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("central_path.png")
    print("Optimization complete. Plot saved as central_path.png")

if __name__ == "__main__":
    demonstrate_barrier_method()
