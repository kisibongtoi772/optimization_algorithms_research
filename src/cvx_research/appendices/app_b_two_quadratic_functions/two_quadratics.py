import numpy as np
import matplotlib.pyplot as plt

def generate_random_symmetric_matrix(n):
    # Generate random matrix
    M = np.random.randn(n, n)
    # Make it symmetric
    return (M + M.T) / 2.0

def plot_numerical_range():
    """
    Visualizes the joint numerical range of two quadratic forms
    A and B on the unit sphere in R^3.
    """
    np.random.seed(42)
    n = 3
    
    A = generate_random_symmetric_matrix(n)
    B = generate_random_symmetric_matrix(n)
    
    # Generate random points on the unit sphere in R^3
    num_points = 50000
    points = np.random.randn(n, num_points)
    # Normalize to lie on the sphere ||x||_2 = 1
    norms = np.linalg.norm(points, axis=0)
    points = points / norms
    
    # Evaluate quadratic forms
    # A_vals[i] = x_i^T A x_i
    A_vals = np.einsum('ij,ji->i', points.T @ A, points)
    B_vals = np.einsum('ij,ji->i', points.T @ B, points)
    
    plt.figure(figsize=(8, 8))
    
    # Scatter plot of the mapped points (x^T A x, x^T B x)
    plt.scatter(A_vals, B_vals, color='purple', alpha=0.3, s=2)
    
    plt.title("Joint Numerical Range of Two Quadratic Forms (n=3)")
    plt.xlabel("$x^T A x$")
    plt.ylabel("$x^T B x$")
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.savefig("numerical_range.png")
    print("Plot saved as numerical_range.png")

if __name__ == "__main__":
    plot_numerical_range()
