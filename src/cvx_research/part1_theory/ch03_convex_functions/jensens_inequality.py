import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """A strictly convex function: f(x) = x^2"""
    return x**2

def df(x):
    """Derivative of the convex function: f'(x) = 2x"""
    return 2 * x

def plot_jensens_inequality():
    """
    Demonstrates Jensen's Inequality: 
    f(theta*x + (1-theta)*y) <= theta*f(x) + (1-theta)*f(y)
    """
    x_vals = np.linspace(-4, 4, 100)
    y_vals = f(x_vals)
    
    # Pick two points
    x1, x2 = -3, 3
    y1, y2 = f(x1), f(x2)
    
    # Pick a theta
    theta = 0.3
    x_theta = theta * x1 + (1 - theta) * x2
    
    # Jensen's components
    lhs = f(x_theta)  # Function evaluated at the combination
    rhs = theta * y1 + (1 - theta) * y2  # Combination of the function evaluations
    
    plt.figure(figsize=(10, 5))
    
    # Plot 1: Jensen's Inequality
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, y_vals, label="f(x) = x^2", color="blue")
    
    # Plot secant line between (x1, y1) and (x2, y2)
    plt.plot([x1, x2], [y1, y2], 'r--', label="Secant line (upper bound)")
    
    # Plot the specific points
    plt.plot(x1, y1, 'ko')
    plt.plot(x2, y2, 'ko')
    plt.plot(x_theta, lhs, 'go', label="f(theta*x + (1-theta)*y)")
    plt.plot(x_theta, rhs, 'mo', label="theta*f(x) + (1-theta)*f(y)")
    plt.vlines(x_theta, ymin=lhs, ymax=rhs, colors='gray', linestyles='dotted')
    
    plt.title("Jensen's Inequality")
    plt.legend()
    plt.grid(True)

    # Plot 2: First-Order Condition
    plt.subplot(1, 2, 2)
    plt.plot(x_vals, y_vals, label="f(x) = x^2", color="blue")
    
    # Tangent at x0 = -1
    x0 = -1
    y0 = f(x0)
    tangent_y = y0 + df(x0) * (x_vals - x0)
    
    plt.plot(x_vals, tangent_y, 'g-', label="Tangent line at x=-1")
    plt.plot(x0, y0, 'ko')
    
    plt.title("First-Order Condition\n(Tangent is Global Underestimator)")
    plt.ylim(-2, 16)
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig("jensens_inequality.png")
    plt.show()

if __name__ == "__main__":
    print("Visualizing Convex Functions...")
    plot_jensens_inequality()
