# Qwen Attempt 2: Fails because it incorrectly computes paths through u by not properly distributing removals (uses r for both children without summing).
import sys
sys.setrecursionlimit(10**5 + 10)

def dfs(u, parent, adj, max_diam, max_down, k):
    children = []
    for v, w in adj[u]:
        if v != parent:
            dfs(v, u, adj, max_diam, max_down, k)
            children.append((v, w))
    if not children:
        max_diam[u][0] = 0
        max_down[u][0] = 0
        return
    for r in range(k + 1):
        for v, w in children:
            if max_down[v][r] != float('-inf'):
                max_down[u][r] = max(max_down[u][r], w + max_down[v][r])
        for v, w in children:
            if max_diam[v][r] != float('-inf'):
                max_diam[u][r] = max(max_diam[u][r], max_diam[v][r])
        # Incorrect: For paths through u, assumes r is used for both, not summed
        if len(children) >= 2:
            vals = [w + max_down[v][r] for v, w in children if max_down[v][r] != float('-inf')]
            if len(vals) >= 2:
                vals.sort(reverse=True)
                max_diam[u][r] = max(max_diam[u][r], vals[0] + vals[1])

n, k = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))
max_diam = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
max_down = [[float('-inf')] * (k + 1) for _ in range(n + 1)]
dfs(1, -1, adj, max_diam, max_down, k)
print(max(max_diam[1]))