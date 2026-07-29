# Chapter 5: Duality

## Overview
Duality is one of the most profound concepts in optimization. Every optimization problem (the **primal** problem) has an associated **dual** problem. 

### Key Concepts
1. **The Lagrangian:** We augment the objective function with a weighted sum of the constraint functions. For a problem with inequality constraints $f_i(x) \le 0$ and equality constraints $h_i(x) = 0$, the Lagrangian is:
   
   $$
   L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{i=1}^p \nu_i h_i(x)
   $$
   
   where $\lambda \ge 0$ and $\nu$ are the **Lagrange multipliers** (or dual variables).

2. **The Lagrange Dual Function:** $g(\lambda, \nu) = \inf_x L(x, \lambda, \nu)$. 
   - $g$ is *always* concave, even if the original primal problem is not convex!
   - $g(\lambda, \nu)$ provides a guaranteed lower bound on the optimal primal value $p^\star$.

3. **Weak and Strong Duality:**
   - **Weak Duality:** The optimal dual value $d^\star$ is always $\le p^\star$. The difference $p^\star - d^\star$ is the "duality gap".
   - **Strong Duality:** $d^\star = p^\star$ (zero duality gap). This usually holds for convex problems that strictly satisfy their constraints (known as **Slater's Condition**).

4. **KKT Conditions:** The Karush-Kuhn-Tucker conditions are the necessary and sufficient conditions for optimality in a convex problem with differentiable functions and strong duality. They include:
   - Primal feasibility
   - Dual feasibility
   - Complementary slackness ($\lambda_i f_i(x) = 0$)
   - Gradient of the Lagrangian with respect to $x$ vanishes.

## Applications & Problems Solved
- **Certificate of Optimality:** Dual variables provide a way to *prove* you have found the optimal solution (by checking if the duality gap is zero).
- **Sensitivity Analysis (Shadow Prices):** The optimal dual variables $\lambda^\star$ indicate exactly how much the optimal objective value would improve if a constraint were relaxed by a small amount. In economics, these are "shadow prices".
- **Algorithm Design:** Many state-of-the-art solvers (like Primal-Dual Interior-Point methods) do not just solve for $x$, they simultaneously solve for $(x, \lambda, \nu)$ using the KKT conditions.

## Code Example
See `kkt_and_duality.py` to see how to:
1. Define and solve a primal linear program.
2. Formulate its theoretical dual problem and solve it.
3. Verify **Strong Duality** (the values are equal).
4. Extract the optimal dual variables (shadow prices) directly from a solver.
