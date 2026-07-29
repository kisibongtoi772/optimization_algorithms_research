# Chapter 2: Convex Sets

## Overview
This chapter introduces the fundamental geometric building blocks of convex optimization: **Convex Sets**. A set is convex if, for any two points within the set, the straight line segment connecting them also lies entirely within the set. 

Mathematically, a set $C$ is convex if for any $x, y \in C$ and any $\theta$ with $0 \le \theta \le 1$, we have:
$$ \theta x + (1 - \theta)y \in C $$

### Key Concepts
1. **Affine Sets:** A set where the line passing through any two distinct points in the set lies entirely in the set. (e.g., lines, planes, hyperplanes).
2. **Convex Sets:** A set where the line *segment* between any two points lies in the set. (e.g., balls, ellipsoids, polyhedra).
3. **Cones (Convex Cones):** A set where any non-negative scalar multiple of a point in the set is also in the set, and it is convex.
4. **Hyperplanes and Halfspaces:** A hyperplane divides a space into two halfspaces. Halfspaces are the most basic convex sets. The intersection of multiple halfspaces forms a polyhedron.
5. **Separating Hyperplane Theorem:** If two convex sets $C$ and $D$ are disjoint ($C \cap D = \emptyset$), then there exists a hyperplane that separates them.

## Applications & Problems Solved
Why do we care about convex sets?
- **Feasible Regions:** In optimization, the "feasible region" (the set of all valid choices that satisfy our constraints) must be a convex set for the problem to be easily solvable. 
- **Classification (Machine Learning):** The Separating Hyperplane Theorem is the direct foundational theory behind Support Vector Machines (SVMs). If we have two classes of data that form disjoint convex hulls, we can find a linear boundary to perfectly separate them.
- **Bounding:** The convex hull of a set of points is the tightest convex set containing those points, often used in computational geometry and for finding worst-case bounds in robust optimization.

## Code Example
See `convex_hulls_and_separations.py` for a visual demonstration of:
1. Constructing a **Convex Hull** from a set of random points.
2. Drawing a **Separating Hyperplane** between two disjoint convex sets.
