def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[x_root] = y_root


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = []
for i in range(m):
    b, e, w = map(int, input().split())
    edges.append((w, b, e))
edges = sorted(edges)
min_weight = 0
for edge in edges:
    w, b, e = edge
    if find(b) != find(e):
        min_weight += w
        union(b, e)
print(min_weight)
