# Appendix A: Mathematical Background

## Overview
This appendix provides the foundational mathematical concepts required to understand convex optimization. A solid grasp of linear algebra and multi-variable calculus is essential before diving into the main parts of the book.

### Key Concepts

1. **Vector Norms:** A norm $\| \cdot \|$ is a function that assigns a strictly positive length or size to each vector in a vector space (except for the zero vector). 
   - **$\ell_1$ norm:** $\|x\|_1 = \sum |x_i|$
   - **$\ell_2$ (Euclidean) norm:** $\|x\|_2 = \sqrt{\sum x_i^2}$
   - **$\ell_\infty$ (Chebyshev) norm:** $\|x\|_\infty = \max |x_i|$

2. **Matrix Norms:** Norms applied to matrices. The most common induced norm is the spectral norm, which is the maximum singular value of the matrix.

3. **Derivatives and Gradients:** For a scalar-valued function $f: \mathbb{R}^n \to \mathbb{R}$, the gradient $\nabla f(x)$ is a column vector of partial derivatives. It points in the direction of the steepest ascent.

4. **Hessian:** The matrix of second-order partial derivatives $\nabla^2 f(x)$. A function is convex if and only if its Hessian is positive semi-definite ($\nabla^2 f(x) \succeq 0$) for all $x$ in its domain.

5. **Chain Rule:** Crucial for calculating gradients and Hessians of composite functions, often encountered when applying affine transformations to variables.

## Code Example
See `norms_and_analysis.py` for a visualization of the **unit balls** associated with the $\ell_1$, $\ell_2$, and $\ell_\infty$ norms in 2D space. The unit ball is the set of all points $x$ such that $\|x\| \le 1$.

![Unit Balls for Various Norms](unit_balls.png)
