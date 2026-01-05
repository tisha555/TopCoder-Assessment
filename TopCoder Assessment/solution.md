The solution uses dynamic programming on the tree with DFS. Define two DP tables:

max_down[u][r]: The maximum length of a path starting from u downward into its subtree, using exactly r removals in the subtree.
max_diam[u][r]: The maximum diameter in the subtree of u, using exactly r removals in the subtree.
For a node u:

Compute max_down[u][r] as the max over children v of (weight(u,v) + max_down[v][r]).
For max_diam[u][r], take the max of:
Diameters from children's subtrees: max over v of max_diam[v][r].
Paths through u: For each r, collect vals = [weight(u,v) + max_down[v][s] for s where max_down[v][s] != -inf], then for each possible s1 + s2 = r with different children, maximize vals[s1] + vals[s2] (handled by sorting vals per r and taking top two if >=2 children).
Leaves: max_diam[u][0] = 0, max_down[u][0] = 0.
The answer is max over r=0 to k of max_diam[1][r]. Time: O(n * k), space: O(n * k). Uses recursion with increased limit for n=1e5.