# Convex Optimization Research Project

This project is dedicated to researching and implementing optimization algorithms, heavily inspired by and following the structure of the renowned book **"Convex Optimization"** by Stephen Boyd and Lieven Vandenberghe.

## Structure

The repository is organized into `src/cvx_research/` (for Python modules) and `notebooks/` (for interactive Jupyter notebooks), both mirroring the book's parts and chapters:

### Part I: Theory
- **Chapter 2:** Convex sets
- **Chapter 3:** Convex functions
- **Chapter 4:** Convex optimization problems
- **Chapter 5:** Duality

### Part II: Applications
- **Chapter 6:** Approximation and fitting
- **Chapter 7:** Statistical estimation
- **Chapter 8:** Geometric problems

### Part III: Algorithms
- **Chapter 9:** Unconstrained minimization
- **Chapter 10:** Equality constrained minimization
- **Chapter 11:** Interior-point methods

### Appendices
- **Appendix A:** Mathematical background
- **Appendix B:** Problems involving two quadratic functions
- **Appendix C:** Numerical linear algebra background

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
