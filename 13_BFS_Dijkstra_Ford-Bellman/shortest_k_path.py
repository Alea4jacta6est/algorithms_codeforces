import sys


def shortest_paths(n, k, s, edges):
    dp = tuple([INF for _ in range(k + 1)] for _ in range(n))
    graph = [[] for _ in range(n)]
    for a, b, w in edges:
        graph[a - 1].append((b - 1, w))
    dp[s - 1][0] = 0
    for j in range(1, k + 1):
        for i in range(n):
            for v, w in graph[i]:
                for k in range(1, j + 1):
                    if dp[i][k - 1] != INF:
                        dp[v][k] = min(dp[v][k], dp[i][k - 1] + w)
    res = [dp[i][k] if dp[i][k] != INF else -1 for i in range(n)]
    return res


n, m, k, s = map(int, input().split())
INF = sys.maxsize
edges = [tuple(map(int, input().split())) for _ in range(m)]
print(" ".join(map(str, shortest_paths(n, k, s, edges))))
