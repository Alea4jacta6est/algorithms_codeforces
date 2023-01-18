import sys

n = int(input())
graph = [input().split() for _ in range(n)]
for i in range(n):
    for j in range(i, n):
        if graph[i][j] != graph[j][i] or (i == j and graph[i][j] == "1"):
            print("NO")
            sys.exit(0)
print("YES")
