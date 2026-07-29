import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt

def demonstrate_logistic_regression():
    """
    Demonstrates Logistic Regression as a Maximum Likelihood Estimation (MLE) 
    problem solved via Convex Optimization.
    """
    np.random.seed(42)
    n = 2     # features
    m = 100   # samples
    
    # Generate synthetic binary classification data
    X1 = np.random.randn(m//2, n) + np.array([2, 2])
    X2 = np.random.randn(m//2, n) + np.array([-2, -2])
    X = np.vstack([X1, X2])
    
    # Labels: 1 for class 1, 0 for class 2
    y = np.hstack([np.ones(m//2), np.zeros(m//2)])
    
    # Variable for the hyperplane parameters
    w = cp.Variable(n)
    b = cp.Variable()
    
    # The negative log-likelihood for logistic regression is:
    # sum( log(1 + exp(X*w + b)) ) - y^T (X*w + b)
    # cvxpy provides cp.logistic(z) which represents log(1 + exp(z))
    logits = X @ w + b
    loss = cp.sum(cp.logistic(logits)) - y.T @ logits
    
    # Solve the problem
    prob = cp.Problem(cp.Minimize(loss))
    prob.solve()
    
    w_val = w.value
    b_val = b.value
    
    # Plotting
    plt.figure(figsize=(8, 6))
    
    # Scatter plot of data points
    plt.scatter(X1[:, 0], X1[:, 1], color='blue', label='Class 1 (y=1)')
    plt.scatter(X2[:, 0], X2[:, 1], color='red', label='Class 0 (y=0)')
    
    # Plot decision boundary: w0*x0 + w1*x1 + b = 0 => x1 = -(w0*x0 + b) / w1
    x_boundary = np.linspace(-4, 4, 100)
    y_boundary = -(w_val[0] * x_boundary + b_val) / w_val[1]
    plt.plot(x_boundary, y_boundary, 'k--', lw=2, label='Decision Boundary')
    
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.title("Logistic Regression (MLE) via Convex Optimization")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("logistic_regression.png")
    print("Optimization complete. Plot saved as logistic_regression.png")

if __name__ == "__main__":
    demonstrate_logistic_regression()
