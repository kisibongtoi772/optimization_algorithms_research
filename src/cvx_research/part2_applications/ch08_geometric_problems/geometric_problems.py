import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

def demonstrate_max_margin_classifier():
    """
    Demonstrates the Maximum Margin Classifier (Linear SVM) 
    as a geometric convex optimization problem.
    """
    np.random.seed(0)
    n = 2     # features
    m = 60    # samples per class
    
    # Generate linearly separable data
    X1 = np.random.randn(m, n) + np.array([2, 2.5])
    X2 = np.random.randn(m, n) + np.array([-2, -2.5])
    X = np.vstack([X1, X2])
    
    # Labels: 1 for class 1, -1 for class 2
    y = np.hstack([np.ones(m), -np.ones(m)])
    
    # Variables
    w = cp.Variable(n)
    b = cp.Variable()
    
    # Objective: Minimize (1/2) * ||w||_2^2
    objective = cp.Minimize(0.5 * cp.sum_squares(w))
    
    # Constraints: y_i * (w^T x_i + b) >= 1
    constraints = [cp.multiply(y, X @ w + b) >= 1]
    
    # Solve
    prob = cp.Problem(objective, constraints)
    prob.solve()
    
    w_val = w.value
    b_val = b.value
    
    # Plotting
    plt.figure(figsize=(8, 6))
    
    # Scatter plot
    plt.scatter(X1[:, 0], X1[:, 1], color='blue', label='Class 1')
    plt.scatter(X2[:, 0], X2[:, 1], color='red', label='Class -1')
    
    # Decision boundary: w^T x + b = 0
    x_boundary = np.linspace(-5, 5, 100)
    y_boundary = -(w_val[0] * x_boundary + b_val) / w_val[1]
    plt.plot(x_boundary, y_boundary, 'k-', lw=2, label='Decision Boundary')
    
    # Margins: w^T x + b = 1 and w^T x + b = -1
    y_margin_pos = -(w_val[0] * x_boundary + b_val - 1) / w_val[1]
    y_margin_neg = -(w_val[0] * x_boundary + b_val + 1) / w_val[1]
    plt.plot(x_boundary, y_margin_pos, 'k--', lw=1, label='Margin +1')
    plt.plot(x_boundary, y_margin_neg, 'k--', lw=1, label='Margin -1')
    
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)
    plt.title("Maximum Margin Classifier (Geometric Separation)")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("max_margin_classifier.png")
    print("Optimization complete. Plot saved as max_margin_classifier.png")

if __name__ == "__main__":
    demonstrate_max_margin_classifier()
