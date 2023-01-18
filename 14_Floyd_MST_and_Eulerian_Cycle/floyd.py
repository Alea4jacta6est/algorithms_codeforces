from sys import stdin


def floyd_warshall(n, graph):
    inf_ = 1 << 32
    distances = [[j if j != None else inf_ for j in i] for i in graph]
    for i in range(n):
        distances[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances


n = int(stdin.readline())
graph = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j, w in enumerate(stdin.readline().split()):
        graph[i][j] = int(w)
distances = floyd_warshall(n, graph)
for item in distances:
    print(" ".join([str(j) for j in item]))
