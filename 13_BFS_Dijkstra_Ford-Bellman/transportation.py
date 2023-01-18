import sys
import heapq


def dijkstra(edges, s, f, weight, visited={}):
    h = [(0, s)]
    while len(h) > 0:
        distance, vertex = heapq.heappop(h)
        if vertex in visited:
            continue
        if vertex == f:
            return distance <= 24 * 60
        visited[vertex] = distance
        for i, t, w in edges[vertex]:
            if i in visited or w < weight:
                continue
            else:
                heapq.heappush(h, (distance + t, i))
    return False


number_of_towns, number_of_roads = [int(x) for x in sys.stdin.readline().split()]
edges = {}
for i in range(number_of_roads):
    a, b, t, w = [int(x) for x in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    if a not in edges:
        edges[a] = []
    if b not in edges:
        edges[b] = []
    edges[a].append((b, t, w))
    edges[b].append((a, t, w))
lcups, rcups = 0, 10**7
while rcups > lcups:
    m = lcups + (rcups - lcups) // 2
    if lcups == m or rcups == m:
        break
    if dijkstra(edges, 0, number_of_towns - 1, m * 100 + 3000000, {}):
        lcups = m
    else:
        rcups = m
if dijkstra(edges, 0, number_of_towns - 1, rcups * 100 + 3000000):
    print(rcups)
else:
    print(lcups)
