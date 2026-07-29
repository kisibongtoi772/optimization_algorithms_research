import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def plot_convex_hull():
    """
    Demonstrates the concept of a Convex Hull.
    The convex hull is the smallest convex set that contains a given set of points.
    Think of it as wrapping a rubber band around a set of pegs.
    """
    # Generate random points
    np.random.seed(42)
    points = np.random.rand(30, 2)

    # Compute Convex Hull
    hull = ConvexHull(points)

    plt.figure(figsize=(8, 6))
    plt.plot(points[:, 0], points[:, 1], 'o', label='Original Points')
    
    # Plot the hull edges
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'r-', lw=2)
    
    # Fill the convex set
    hull_points = points[hull.vertices, :]
    plt.fill(hull_points[:, 0], hull_points[:, 1], alpha=0.3, color='red', label='Convex Hull (Convex Set)')
    
    plt.title("Convex Hull of Random Points")
    plt.legend()
    plt.grid(True)
    plt.savefig("convex_hull.png")
    plt.show()

def plot_separating_hyperplane():
    """
    Demonstrates the Separating Hyperplane Theorem.
    If two convex sets are disjoint, there exists a hyperplane (a line in 2D)
    that separates them.
    """
    # Generate two disjoint sets of points (representing two convex sets)
    np.random.seed(0)
    set1 = np.random.randn(20, 2) * 0.5 + np.array([2, 2])
    set2 = np.random.randn(20, 2) * 0.5 + np.array([5, 5])
    
    hull1 = ConvexHull(set1)
    hull2 = ConvexHull(set2)

    plt.figure(figsize=(8, 6))
    
    # Plot Set 1
    plt.plot(set1[:, 0], set1[:, 1], 'bo', label='Set 1 Points')
    plt.fill(set1[hull1.vertices, 0], set1[hull1.vertices, 1], alpha=0.3, color='blue', label='Convex Set 1')
    
    # Plot Set 2
    plt.plot(set2[:, 0], set2[:, 1], 'go', label='Set 2 Points')
    plt.fill(set2[hull2.vertices, 0], set2[hull2.vertices, 1], alpha=0.3, color='green', label='Convex Set 2')

    # Draw a manually calculated separating hyperplane
    # For means [2,2] and [5,5], the midpoint is [3.5, 3.5]
    # The vector between means is [3, 3]. Orthogonal vector is [-1, 1].
    # So the line is x + y = 7 -> y = -x + 7
    x_vals = np.linspace(0, 7, 100)
    y_vals = -x_vals + 7
    
    plt.plot(x_vals, y_vals, 'r--', lw=2, label='Separating Hyperplane')
    
    plt.title("Separating Hyperplane Theorem")
    plt.xlim(0, 7)
    plt.ylim(0, 7)
    plt.legend()
    plt.grid(True)
    plt.savefig("separating_hyperplane.png")
    plt.show()

if __name__ == "__main__":
    print("Plotting Convex Hull...")
    plot_convex_hull()
    
    print("Plotting Separating Hyperplane...")
    plot_separating_hyperplane()
