Maximizing Tree Diameter with Removals
You are given a tree with n nodes, rooted at node 1. Each edge has a positive weight. You can remove up to k nodes from the tree (the root cannot be removed). After removals, the remaining graph is a forest, and you must consider only the component containing the root. The diameter of this component is the maximum sum of edge weights along any path in it. Find the maximum possible diameter achievable by removing at most k nodes.

Input
The first line contains two integers n and k (1 ≤ n ≤ 10^5, 0 ≤ k ≤ 20).
The next n-1 lines each contain three integers u, v, w (1 ≤ u, v ≤ n, 1 ≤ w ≤ 10^9), describing an edge between u and v with weight w.
Output
A single integer: the maximum possible diameter.


Examples
Input:
3 0
1 2 1
2 3 2
Output:
3


Input:
3 1
1 2 1
2 3 2
Output:
3