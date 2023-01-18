import sys


def is_bipartite(n, graph):
    bipartite_states = [-1] * (n)
    q = []
    for i in range(n):
        if bipartite_states[i] == -1:
            q.append([i, 0])
            bipartite_states[i] = 0
            while len(q) != 0:
                p = q[0]
                q.pop(0)
                v = p[0]
                c = p[1]
                for j in graph[v]:
                    if bipartite_states[j] == c:
                        return False, bipartite_states
                    if bipartite_states[j] == -1:
                        if c == 1:
                            bipartite_states[j] = 0
                        else:
                            bipartite_states[j] = 1
                        q.append([j, bipartite_states[j]])
    return True, [str(i + 1) for i in bipartite_states]


n, m = [int(x) for x in sys.stdin.readline().split()]
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(x) for x in sys.stdin.readline().split()]
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
out = is_bipartite(n, graph)
if out[0]:
    print("YES")
    print(" ".join(out[1]))
else:
    print("NO")
