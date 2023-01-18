from collections import deque
from sys import stdin


def find_distances(n, x, graph):
    distances = [float("inf") for _ in range(n)]
    distances[x - 1] = 0
    queue = deque([x - 1])
    # BFS
    while queue:
        vertex = queue.popleft()
        for neighbor in range(n):
            if graph[vertex][neighbor] and distances[neighbor] == float("inf"):
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    return [
        str(-1) if distance == float("inf") else str(distance) for distance in distances
    ]


n, x = [int(x) for x in stdin.readline().strip().split()]
graph = [[int(_) for _ in item.split()] for item in stdin.readlines()]
print(" ".join(find_distances(n, x, graph)))
