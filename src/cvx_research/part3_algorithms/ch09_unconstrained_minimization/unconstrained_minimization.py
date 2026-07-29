import numpy as np
import matplotlib.pyplot as plt

def f(x, P, q):
    return 0.5 * x.T @ P @ x + q.T @ x

def grad_f(x, P, q):
    return P @ x + q

def hessian_f(x, P):
    return P

def backtracking_line_search(x, dx, P, q, alpha=0.1, beta=0.7):
    t = 1.0
    val_x = f(x, P, q)
    grad_x = grad_f(x, P, q)
    
    while f(x + t * dx, P, q) > val_x + alpha * t * grad_x.T @ dx:
        t *= beta
    return t

def gradient_descent(x0, P, q, iters=30):
    x = x0.copy()
    path = [x.copy()]
    for _ in range(iters):
        dx = -grad_f(x, P, q)
        t = backtracking_line_search(x, dx, P, q)
        x = x + t * dx
        path.append(x.copy())
    return np.array(path)

def newtons_method(x0, P, q, iters=5):
    x = x0.copy()
    path = [x.copy()]
    for _ in range(iters):
        g = grad_f(x, P, q)
        H = hessian_f(x, P)
        dx = -np.linalg.solve(H, g)
        t = backtracking_line_search(x, dx, P, q)
        x = x + t * dx
        path.append(x.copy())
    return np.array(path)

def demonstrate_algorithms():
    # Define a poorly conditioned quadratic problem
    # P must be symmetric positive definite
    P = np.array([[20.0, 0.0], 
                  [0.0, 1.0]])
    q = np.array([0.0, 0.0])
    
    x0 = np.array([8.0, 8.0])
    
    path_gd = gradient_descent(x0, P, q, iters=40)
    path_nt = newtons_method(x0, P, q, iters=5)
    
    # Plotting
    X1, X2 = np.meshgrid(np.linspace(-10, 10, 100), np.linspace(-10, 10, 100))
    Z = 0.5 * (P[0,0]*X1**2 + P[1,1]*X2**2)
    
    plt.figure(figsize=(10, 8))
    plt.contour(X1, X2, Z, levels=np.logspace(0, 3, 20), cmap='viridis', alpha=0.5)
    
    # Plot paths
    plt.plot(path_gd[:, 0], path_gd[:, 1], 'ro-', markersize=4, label='Gradient Descent')
    plt.plot(path_nt[:, 0], path_nt[:, 1], 'bs-', markersize=6, label="Newton's Method")
    
    # Optimum
    plt.plot(0, 0, 'k*', markersize=15, label='Optimum')
    
    plt.title("Gradient Descent vs Newton's Method")
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("descent_paths.png")
    print("Optimization complete. Plot saved as descent_paths.png")

if __name__ == "__main__":
    demonstrate_algorithms()
