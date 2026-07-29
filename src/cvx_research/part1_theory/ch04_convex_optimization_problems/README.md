# Chapter 4: Convex Optimization Problems

## Overview
A mathematical optimization problem is a **convex optimization problem** if it can be written in the standard form:

$$
\begin{align*}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \le 0, \quad i = 1, \dots, m \\
& h_i(x) = 0, \quad i = 1, \dots, p
\end{align*}
$$

where:
- The objective function $f_0$ is a convex function.
- The inequality constraint functions $f_i$ are convex functions.
- The equality constraint functions $h_i$ are affine functions ($h_i(x) = a_i^Tx - b_i$).

Because the intersection of convex sets is convex, the feasible region of a convex optimization problem is a convex set. Combined with a convex objective function, this guarantees that any local minimum is a global minimum.

### Problem Classes (Hierarchy)
Convex optimization problems are classified by the algebraic forms of their objective and constraint functions. There is a hierarchy where each class generalizes the previous one:
1. **Linear Programming (LP):** Objective and all constraints are affine (linear).
2. **Quadratic Programming (QP):** Objective is convex quadratic, constraints are affine.
3. **Quadratically Constrained Quadratic Programming (QCQP):** Objective and inequality constraints are convex quadratic.
4. **Second-Order Cone Programming (SOCP):** Includes constraints representing the norm of a vector (ice-cream cones).
5. **Semidefinite Programming (SDP):** The variable is a symmetric matrix, and constraints force it to be positive semi-definite (LMI - Linear Matrix Inequalities).

## Applications & Problems Solved
- **Operations Research (LP):** Supply chain routing, the diet problem, scheduling, and resource allocation.
- **Finance (QP):** Markowitz Portfolio Optimization (minimizing variance/risk while achieving a target return).
- **Machine Learning (QP & SOCP):** Support Vector Machines (QP), robust regression (SOCP).
- **Control Theory (SDP):** Synthesizing controllers for dynamical systems (e.g., LQR) and proving system stability via Lyapunov functions.

## Code Example
See `standard_forms.py` for a demonstration of formulating and solving these problems using `CVXPY`, a Python-embedded modeling language for convex optimization problems:
1. Solving a simple **Linear Program (LP)**.
2. Solving a simple **Quadratic Program (QP)** (constrained least squares).
