import random

n = random.randint(10, 100)
k = random.randint(0, 5)
print(n, k)
edges = []
for i in range(2, n + 1):
    parent = random.randint(1, i - 1)
    w = random.randint(1, 10)
    edges.append((parent, i, w))
random.shuffle(edges)
for u, v, w in edges:
    print(u, v, w)