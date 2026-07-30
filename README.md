# Convex Optimization Research Project

This project is dedicated to researching and implementing optimization algorithms, heavily inspired by and following the structure of the renowned book **"Convex Optimization"** by Stephen Boyd and Lieven Vandenberghe.

## Structure

The repository is organized into `src/cvx_research/` (for Python modules) and `notebooks/` (for interactive Jupyter notebooks), both mirroring the book's parts and chapters. Below is a visual summary of the topics covered:

### Part I: Theory

**Chapter 2: Convex Sets**  
Explores the foundational geometric properties of convex sets, convex hulls, and separating hyperplanes.  
![Convex Hull](src/cvx_research/part1_theory/ch02_convex_sets/convex_hull.png)

**Chapter 3: Convex Functions**  
Analyzes the properties of convex functions, including Jensen's inequality and epigraphs.  
![Jensen's Inequality](src/cvx_research/part1_theory/ch03_convex_functions/jensens_inequality.png)

**Chapter 4: Convex Optimization Problems**  
Focuses on standard forms of optimization problems, such as linear programming (LP) and quadratic programming (QP).

**Chapter 5: Duality**  
Introduces Lagrange dual functions, weak and strong duality, and the Karush-Kuhn-Tucker (KKT) conditions.

### Part II: Applications

**Chapter 6: Approximation and Fitting**  
Covers norm approximation, least-norm problems, and robust penalty functions for data fitting.  
![Approximation](src/cvx_research/part2_applications/ch06_approximation_and_fitting/approximation.png)

**Chapter 7: Statistical Estimation**  
Applies convex optimization to maximum likelihood estimation, including logistic regression.  
![Logistic Regression](src/cvx_research/part2_applications/ch07_statistical_estimation/logistic_regression.png)

**Chapter 8: Geometric Problems**  
Solves geometric problems such as finding maximum margin classifiers (SVMs) and extreme points.  
![Max Margin Classifier](src/cvx_research/part2_applications/ch08_geometric_problems/max_margin_classifier.png)

### Part III: Algorithms

**Chapter 9: Unconstrained Minimization**  
Implements iterative methods like Gradient Descent, Steepest Descent, and Newton's Method.  
![Descent Paths](src/cvx_research/part3_algorithms/ch09_unconstrained_minimization/descent_paths.png)

**Chapter 10: Equality Constrained Minimization**  
Extends Newton's method to handle equality constraints via KKT systems and variable elimination.  
![Equality Constrained](src/cvx_research/part3_algorithms/ch10_equality_constrained_minimization/equality_constrained.png)

**Chapter 11: Interior-point Methods**  
Solves inequality constrained problems using the barrier method, following the central path.  
![Central Path](src/cvx_research/part3_algorithms/ch11_interior_point_methods/central_path.png)

### Appendices

**Appendix A: Mathematical Background**  
Reviews essential mathematical concepts such as norms, analysis, and unit balls.  
![Unit Balls](src/cvx_research/appendices/app_a_mathematical_background/unit_balls.png)

**Appendix B: Problems Involving Two Quadratic Functions**  
Explores the S-procedure and the numerical range of two quadratic functions.  
![Numerical Range](src/cvx_research/appendices/app_b_two_quadratic_functions/numerical_range.png)

**Appendix C: Numerical Linear Algebra Background**  
Covers matrix factorizations like Cholesky, LU, and Singular Value Decomposition (SVD).  
![SVD Transformation](src/cvx_research/appendices/app_c_numerical_linear_algebra/svd_transformation.png)

## Requirements

This project uses Python. The core dependencies include:
- `numpy`
- `scipy`
- `matplotlib`
- `cvxpy`
- `jupyter`

## Setup

You can install the dependencies using standard pip or `uv`:

```bash
# Using pip
pip install -e .

# Using uv
uv venv
source .venv/bin/activate
uv pip install -e .
```
