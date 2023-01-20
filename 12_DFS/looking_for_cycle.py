def main():
    def dfs(v, visited, graph, time_out, time):
        visited[v] = 1
        for i in graph[v]:
            if visited[i] == -1:
                ret_code, vertex = dfs(i, visited, graph, time_out, time)
                if ret_code == 1:
                    res.append(v + 1)
                    if v == vertex:
                        print("YES")
                        for j in res[::-1]:
                            print(j, end=" ")
                        exit(0)
                    return 1, vertex
            elif time_out[i] == 0:
                res.append(v + 1)
                return 1, i
        time["t"] += 1
        time_out[v] = time["t"]
        return 0, -1

    n, m = [int(x) for x in sys.stdin.readline().split()]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = [int(x) for x in sys.stdin.readline().split()]
        a -= 1
        b -= 1
        graph[a].append(b)
    res = []
    visited = [-1 for _ in range(n)]
    time_out = [0 for _ in range(n)]
    time = {"t": 0}
    col = 0
    for i in range(n):
        if visited[i] == -1:
            ret_code, vertex = DFS(i, visited, graph, time_out, time)
            if ret_code == 1 and i == vertex:
                print("YES")
                for j in res[::-1]:
                    print(j, end=" ")
                exit(0)

    print("NO")


import sys, threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
