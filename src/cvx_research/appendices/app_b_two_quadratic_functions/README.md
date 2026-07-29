# Appendix B: Problems Involving Two Quadratic Functions

## Overview
This appendix deals with a fascinating exception in optimization: certain non-convex problems involving exactly two quadratic functions can actually be solved exactly using convex optimization techniques.

### Key Concepts

1. **The S-Procedure:** Suppose we have two symmetric matrices $A$ and $B$. We want to know if the condition $x^T B x \ge 0 \implies x^T A x \ge 0$ holds. A sufficient condition is that there exists a $\lambda \ge 0$ such that $A \succeq \lambda B$. The **S-procedure** states that for $m=1$ (one constraint), this condition is also **necessary** (lossless), provided there is a point where $x^T B x > 0$. This allows us to convert non-convex quadratic implications into convex Linear Matrix Inequalities (LMIs).

2. **Numerical Range of Two Quadratic Forms:** Let $A, B \in \mathbb{S}^n$. The set of values taken by the two quadratic forms evaluated on the unit sphere:
   
$$
R = \{ (x^T A x, x^T B x) \mid \|x\|_2 = 1 \}
$$

   By a famous theorem (Dines, Toeplitz-Hausdorff), for $n \ge 3$, this set $R$ is **always convex**, even though the mapping itself is highly non-linear (quadratic) and the domain (the unit sphere) is not a convex set. 

3. **Hidden Convexity:** Because the joint numerical range of two quadratic forms is convex, minimizing a quadratic function subject to a single quadratic equality or inequality constraint can be solved exactly via its dual semidefinite program (SDP). There is zero duality gap.

## Code Example
See `two_quadratics.py` for a visualization of the **joint numerical range** of two quadratic forms $A$ and $B$ evaluated on points sampled uniformly from the 3D unit sphere. You will clearly see that the resulting shape in 2D space is perfectly convex (a filled ellipse).

![Joint Numerical Range](numerical_range.png)
