# Chapter 11: Interior-Point Methods

## Overview
This chapter introduces **Interior-Point Methods**, which are algorithms that solve convex optimization problems with both inequality and equality constraints:

$$
\begin{array}{ll}
\text{minimize} & f_0(x) \\
\text{subject to} & f_i(x) \le 0, \quad i=1,\dots,m \\
                  & Ax = b
\end{array}
$$

These methods work by reducing the constrained problem to a sequence of unconstrained (or equality constrained) problems, which are then solved using Newton's method (from Chapters 9 and 10).

### Key Concepts

1. **The Logarithmic Barrier:** We can replace the inequality constraints with an indicator function that is $0$ if $f_i(x) \le 0$ and $\infty$ otherwise. To make this smooth and differentiable, we approximate the indicator function with a logarithmic barrier:

$$
\phi(x) = -\sum_{i=1}^m \log(-f_i(x))
$$

   This function approaches infinity as $x$ approaches the boundary of the feasible set, forcing the iterates to stay strictly inside the interior (hence "interior-point").

2. **The Central Path:** We form the unconstrained (or equality constrained) objective $t f_0(x) + \phi(x)$, where $t > 0$ is a parameter that controls the accuracy of the approximation. For each $t$, the unique minimizer is denoted $x^\star(t)$. The curve formed by $x^\star(t)$ as $t$ varies from $0$ to $\infty$ is called the **central path**.

3. **The Barrier Method:** 
   - Start with a strictly feasible $x$ and $t > 0$.
   - **Centering step:** Compute $x^\star(t)$ by minimizing $t f_0(x) + \phi(x)$ using Newton's method, starting from the current $x$.
   - **Update:** $x \leftarrow x^\star(t)$.
   - **Increase $t$:** $t \leftarrow \mu t$ (where $\mu > 1$, typically between 10 and 20).
   - Repeat until the duality gap $m/t$ is less than a desired tolerance $\epsilon$.

4. **Primal-Dual Interior-Point Methods:** Instead of two nested loops (outer for $t$, inner for Newton), these methods update the primal variables $x$ and dual variables $(\lambda, \nu)$ simultaneously. They are typically faster and more robust than the standard barrier method and are used in almost all commercial solvers.

## Applications & Problems Solved
- **General Convex Optimization:** Interior-point methods are the universal engines for solving LPs, QPs, SOCPs, and SDPs efficiently in polynomial time.
- **Large-scale Problems:** When combined with sparse linear algebra, they can solve problems with millions of variables.

## Code Example
See `interior_point_methods.py` for an implementation of the **Barrier Method** applied to a Linear Program (LP). We minimize $c^T x$ subject to $Ax \le b$. The plot shows the feasible region (a polyhedron) and the trajectory of the **central path** converging to the optimal vertex as the barrier parameter $t$ increases.

![Barrier Method Central Path](central_path.png)
