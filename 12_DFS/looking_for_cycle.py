import sys
import threading

sys.setrecursionlimit(10 * 7)
threading.stack_size(1 << 27)


def run():
    def dfs(v, visited, graph, counter, time):
        visited[v] = 1
        for i in graph[v]:
            if visited[i] == -1:
                st, vertex = dfs(i, visited, graph, counter, time)
                if st == 1:
                    output.append(v + 1)
                    if v == vertex:
                        print("YES")
                        for j in output[::-1]:
                            print(j, end=" ")
                        exit(0)
                    return 1, vertex
            elif counter[i] == 0:
                output.append(v + 1)
                return 1, i
        time["c"] += 1
        counter[v] = time["c"]
        return 0, -1

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        v, u = [int(_) for _ in sys.stdin.readline().split()]
        v -= 1
        u -= 1
        graph[v].append(u)
    output = []
    counter, visited = [0 for _ in range(n)], [-1 for _ in range(n)]
    for i in range(n):
        if visited[i] == -1:
            st, vertex = dfs(i, visited, graph, counter, {"c": 0})
            if st == 1 and i == vertex:
                print("YES")
                for v in output:
                    print(v, end=" ")
                exit(0)
    print("NO")


thread = threading.Thread(target=run)
thread.start()
thread.join()
