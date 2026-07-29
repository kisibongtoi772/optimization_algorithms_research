import numpy as np
import matplotlib.pyplot as plt
import cvxpy as cp

def demonstrate_norm_approximation():
    """
    Demonstrates the difference between L2 (Least Squares) and 
    L1 (Robust) norm approximation in the presence of outliers.
    """
    # 1. Generate synthetic data (a straight line with noise)
    np.random.seed(42)
    m = 50  # Number of data points
    n = 2   # Number of features (slope and intercept)
    
    # x values from 0 to 10
    x_data = np.linspace(0, 10, m)
    
    # True parameters: slope = 2, intercept = 1
    true_theta = np.array([2.0, 1.0])
    
    # Construct A matrix for A * theta = b
    A = np.vstack([x_data, np.ones(m)]).T
    
    # Generate b with small Gaussian noise
    b = A @ true_theta + np.random.randn(m) * 0.5
    
    # Add severe outliers to the data
    b[40] -= 15
    b[42] -= 20
    b[45] += 18
    b[48] += 25

    # 2. L2 Norm Approximation (Least Squares)
    theta_l2 = cp.Variable(n)
    cost_l2 = cp.sum_squares(A @ theta_l2 - b)
    prob_l2 = cp.Problem(cp.Minimize(cost_l2))
    prob_l2.solve()
    
    # 3. L1 Norm Approximation (Robust Approximation)
    theta_l1 = cp.Variable(n)
    cost_l1 = cp.norm1(A @ theta_l1 - b)
    prob_l1 = cp.Problem(cp.Minimize(cost_l1))
    prob_l1.solve()

    # 4. Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(x_data, b, 'ko', label='Data with outliers', markersize=5)
    
    # True line
    plt.plot(x_data, A @ true_theta, 'g-', lw=2, label='True Line')
    
    # L2 line
    plt.plot(x_data, A @ theta_l2.value, 'r--', lw=2, label='L2 Approximation (Least Squares)')
    
    # L1 line
    plt.plot(x_data, A @ theta_l1.value, 'b-.', lw=2, label='L1 Approximation (Robust)')
    
    plt.title("Norm Approximation: L1 vs L2 in the presence of outliers")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig("approximation.png")
    
    print("Approximation complete. Plot saved as approximation.png")

if __name__ == "__main__":
    demonstrate_norm_approximation()
