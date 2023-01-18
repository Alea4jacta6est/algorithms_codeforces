import threading
import sys


def run():
    def print(s):
        sys.stdout.write(str(s) + " ")

    def dfs(n, graph):
        visited = {i: False for i in range(1, n + 1)}
        stack, components = [], []
        for v in range(1, n + 1):
            if not visited[v]:
                current_component = set()
                stack.append(v)
                visited[v] = True
                while stack:
                    vertex = stack.pop()
                    current_component.add(vertex)
                    for neighbor in graph[vertex]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
                            visited[neighbor] = True
                components.append(current_component)
        return len(components), components

    n, _ = map(int, sys.stdin.readline().split())
    edges = [map(int, item.split()) for item in sys.stdin.readlines()]
    graph = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    k, components = dfs(n, graph)
    print(f"{k}\n")
    for i in range(1, n + 1):
        for j in range(k):
            if i in components[j]:
                print(j + 1)


main_thread = threading.Thread(target=run)
main_thread.start()
main_thread.join()
