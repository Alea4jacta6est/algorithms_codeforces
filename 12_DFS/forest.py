from sys import stdin


def is_tree(n, matrix):
    edges = 0
    for i in range(n):
        for j in range(n):
            edges += matrix[i][j]
    edges = edges // 2
    if edges != n - 1:
        return "NO"
    visited, queue = [True] + [False] * (n - 1), []
    queue.append(0)
    while queue:
        current = queue.pop(0)
        for i in range(n):
            if matrix[current][i] and not visited[i]:
                visited[i] = True
                queue.append(i)
    for i in visited:
        if not i:
            return "NO"
    return "YES"


n = int(input())
matrix = [[int(_) for _ in item.split()] for item in stdin.readlines()]
print(is_tree(n, matrix))
