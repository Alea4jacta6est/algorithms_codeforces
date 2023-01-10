n, m = map(int, input().split())
acid_level = []
for _ in range(n):
    acid_level.append(list(map(int, input().split())))
damage = [[0 for _ in range(m)] for _ in range(n)]
damage[0][0] = acid_level[0][0]
for i in range(1, n):
    damage[i][0] = damage[i - 1][0] + acid_level[i][0]
for j in range(1, m):
    damage[0][j] = damage[0][j - 1] + acid_level[0][j]
for i in range(1, n):
    for j in range(1, m):
        damage[i][j] = min(damage[i - 1][j], damage[i][j - 1]) + acid_level[i][j]

print(damage[n - 1][m - 1])
