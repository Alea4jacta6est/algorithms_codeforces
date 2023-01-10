n, k = map(int, input().split())
unique_ways = [0 for _ in range(n + 1)]
unique_ways[1] = 1
for i in range(2, n + 1):
    for j in range(1, min(i, k + 1)):
        unique_ways[i] += unique_ways[i - j]
print(unique_ways[n])
