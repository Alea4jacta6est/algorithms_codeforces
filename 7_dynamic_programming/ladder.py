n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
max_sums = [0 for _ in range(n + 1)]
max_sums[0], max_sums[1] = a[0], a[1]
for i in range(2, n + 1):
    max_sums[i] = max(max_sums[i - 1], max_sums[i - 2]) + a[i]
print(max_sums[n])
# 2
# 2 -1
# Output:
# 1
