n, m = [int(i) for i in input().split()]
object_weights = [int(i) for i in input().split()]
values = [int(i) for i in input().split()]
arr = [[None] * (m + 1) for _ in range(n + 1)]
dp = [[-1] * (m + 1) for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 0

for i in range(1, n + 1):
    for w in range(1, m + 1):
        if dp[i - 1][w] != -1:
            dp[i][w] = dp[i - 1][w]
            arr[i][w] = False
        if w >= object_weights[i - 1] and dp[i - 1][w - object_weights[i - 1]] != -1:
            if dp[i - 1][w - object_weights[i - 1]] + values[i - 1] > dp[i - 1][w]:
                dp[i][w] = dp[i - 1][w - object_weights[i - 1]] + values[i - 1]
                arr[i][w] = True
max_cost, weight = 0, 0
for w, c in enumerate(dp[n]):
    if c > max_cost:
        max_cost = c
        weight = w
current, items = [n, weight], []
while arr[current[0]][current[1]] is not None:
    took = arr[current[0]][current[1]]
    if took:
        items.append(current[0])
        current[1] -= object_weights[current[0] - 1]
    current[0] -= 1
print(len(items))
for item in sorted(items):
    print(item, end=" ")
