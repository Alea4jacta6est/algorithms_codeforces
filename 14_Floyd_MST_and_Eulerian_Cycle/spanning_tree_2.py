from sys import stdin
import threading


def run():
    def prim(n, points):
        visited, min_dist, prev = [0] * n, [0] + [float("inf")] * (n - 1), [None] * n
        queue = list(range(n))
        while queue:
            u = queue.pop(0)
            if visited[u]:
                continue
            visited[u] = 1
            for v, point in enumerate(points):
                if visited[v]:
                    continue
                edge_dist = (
                    (points[u][0] - point[0]) ** 2 + (points[u][1] - point[1]) ** 2
                ) ** 0.5
                if edge_dist < min_dist[v]:
                    min_dist[v] = edge_dist
                    prev[v] = u
            queue.sort(key=lambda x: min_dist[x])
        total_weight = sum(min_dist)
        return total_weight

    n = int(input())
    points = tuple([int(_) for _ in item.split()] for item in stdin.readlines())
    print(prim(n, points))


thread = threading.Thread(target=run)
thread.start()
thread.join()
"""
2
0 0
1 1
OUTPUT:
1.4142135624
"""
