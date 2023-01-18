from sys import stdin


def shortestPath(graph, u, v, k):
    V = 4
    if k == 0 and u == v:
        return 0
    if k == 1 and graph[u][v] != INF:
        return graph[u][v]
    if k <= 0:
        return INF

    # Initialize result
    res = INF

    # Go to all adjacents of u and recur
    for i in range(V):
        if graph[u][i] != INF and u != i and v != i:
            rec_res = shortestPath(graph, i, v, k - 1)
            if rec_res != INF:
                res = min(res, graph[u][i] + rec_res)
    return res


INF = 999999999999
n, m, k, s = map(int, input().split())
graph = [[INF for _ in range(m)] for _ in range(n)]
for _ in range(m):
    e, b, w = [int(_) for _ in stdin.readline().split()]
    e -= 1
    b -= 1
    graph[e][b] = w
    graph[b][e] = w
result = shortestPath(graph, s, n - 1, k)
print(result)
# for i in range(n):
#     if result[i] == float("inf"):
#         print(-1)
#     else:
#         print(result[i])
