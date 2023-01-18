from collections import defaultdict


def topological_sort(n, edges):
    indegrees = [0] * n
    graph = defaultdict(list)
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        indegrees[v] += 1
    queue = []
    for i in range(n):
        if indegrees[i] == 0:
            queue.append(i)
    topological_ordering = []
    while queue:
        node = queue.pop(0)
        topological_ordering.append(node)
        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    if len(topological_ordering) == n:
        return topological_ordering
    else:
        return -1


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
result = topological_sort(n, edges)
if result == -1:
    print("-1")
else:
    print(" ".join([str(x + 1) for x in result]))
