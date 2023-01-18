from sys import stdin
import heapq


def dijkstra(n, adj_matrix, s, f, visited={}):
    h = [(0, s)]
    while len(h) > 0:
        distance, vertex = heapq.heappop(h)
        if vertex in visited:
            continue
        if vertex == f:
            return distance
        visited[vertex] = distance
        for i in range(n):
            if i in visited or adj_matrix[vertex][i] == -1:
                continue
            else:
                heapq.heappush(h, (distance + adj_matrix[vertex][i], i))
    return -1


n, s, f = [int(x) for x in stdin.readline().strip().split()]
adj_matrix = [[int(x) for x in stdin.readline().strip().split()] for _ in range(n)]
s -= 1
f -= 1
output = dijkstra(n, adj_matrix, s, f)
print(output)
