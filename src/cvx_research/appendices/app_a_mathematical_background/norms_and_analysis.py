import numpy as np
import matplotlib.pyplot as plt

def plot_unit_balls():
    """
    Visualizes the unit balls for L1, L2, and L-infinity norms in 2D.
    """
    plt.figure(figsize=(8, 8))
    
    # Grid of points
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-1.5, 1.5, 400)
    X, Y = np.meshgrid(x, y)
    
    # L1 norm: |x| + |y| <= 1
    Z_l1 = np.abs(X) + np.abs(Y)
    
    # L2 norm: sqrt(x^2 + y^2) <= 1
    Z_l2 = np.sqrt(X**2 + Y**2)
    
    # L-inf norm: max(|x|, |y|) <= 1
    Z_linf = np.maximum(np.abs(X), np.abs(Y))
    
    # Plotting L-inf norm (largest ball)
    plt.contourf(X, Y, Z_linf, levels=[0, 1], colors=['lightblue'], alpha=0.3)
    plt.contour(X, Y, Z_linf, levels=[1], colors=['blue'], linewidths=2)
    
    # Plotting L2 norm
    plt.contourf(X, Y, Z_l2, levels=[0, 1], colors=['lightgreen'], alpha=0.4)
    plt.contour(X, Y, Z_l2, levels=[1], colors=['green'], linewidths=2)
    
    # Plotting L1 norm (smallest ball)
    plt.contourf(X, Y, Z_l1, levels=[0, 1], colors=['salmon'], alpha=0.5)
    plt.contour(X, Y, Z_l1, levels=[1], colors=['red'], linewidths=2)
    
    # Customizing the plot
    # Dummy lines for legend
    plt.plot([], [], color='blue', linewidth=2, label='$\ell_\infty$ Norm Unit Ball')
    plt.plot([], [], color='green', linewidth=2, label='$\ell_2$ Norm Unit Ball')
    plt.plot([], [], color='red', linewidth=2, label='$\ell_1$ Norm Unit Ball')
    
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    
    plt.title("Unit Balls for Various Norms in $\mathbb{R}^2$")
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    
    plt.savefig("unit_balls.png")
    print("Plot saved as unit_balls.png")

if __name__ == "__main__":
    plot_unit_balls()
