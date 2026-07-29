import numpy as np
import matplotlib.pyplot as plt

def plot_circle(ax, points, color='blue', title=''):
    ax.plot(points[0, :], points[1, :], color=color, lw=2)
    
    # Plot standard basis vectors to see how they rotate
    ax.arrow(0, 0, points[0, 0], points[1, 0], head_width=0.1, color='red', lw=2)
    ax.arrow(0, 0, points[0, 25], points[1, 25], head_width=0.1, color='green', lw=2)
    
    ax.set_aspect('equal')
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title(title)
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)

def demonstrate_svd():
    """
    Geometrically demonstrates the SVD of a 2x2 matrix: A = U * Sigma * V^T
    """
    # Create a unit circle
    theta = np.linspace(0, 2*np.pi, 100)
    circle = np.vstack([np.cos(theta), np.sin(theta)])
    
    # Define a 2x2 matrix A
    A = np.array([[1.5, 0.5], 
                  [-1.0, 2.0]])
    
    # Compute SVD
    U, S, VT = np.linalg.svd(A)
    Sigma = np.diag(S)
    
    # Step-by-step transformations
    # 1. V^T applied to the circle (Rotation)
    circle_vt = VT @ circle
    
    # 2. Sigma applied to the result (Scaling)
    circle_sigma = Sigma @ circle_vt
    
    # 3. U applied to the result (Rotation) -> This equals A * circle
    circle_u = U @ circle_sigma
    
    # Plotting
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))
    
    plot_circle(axes[0], circle, color='blue', title='Original Unit Circle ($x$)')
    plot_circle(axes[1], circle_vt, color='purple', title='1. Rotation ($V^T x$)')
    plot_circle(axes[2], circle_sigma, color='orange', title='2. Scaling ($\Sigma V^T x$)')
    plot_circle(axes[3], circle_u, color='red', title='3. Rotation ($U \Sigma V^T x = Ax$)')
    
    plt.tight_layout()
    plt.savefig("svd_transformation.png", dpi=150)
    print("Plot saved as svd_transformation.png")

if __name__ == "__main__":
    demonstrate_svd()
