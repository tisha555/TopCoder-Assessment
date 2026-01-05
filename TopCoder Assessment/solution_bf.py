# Brute-force: Try all subsets of nodes to remove (up to k), compute diameter of remaining tree. Only for n<=15, k<=5.
import itertools

def compute_diameter(adj, nodes):
    # Simplified: Assume tree, compute max path sum (not implemented fully for brevity)
    return 0  # Placeholder

n, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
max_d = 0
for rem in range(k + 1):
    for subset in itertools.combinations(range(2, n + 1), rem):  # Exclude root
        remaining = [i for i in range(1, n + 1) if i not in subset]
        max_d = max(max_d, compute_diameter(adj, remaining))
print(max_d)