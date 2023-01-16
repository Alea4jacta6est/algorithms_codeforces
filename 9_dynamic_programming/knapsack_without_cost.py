s, n = map(int, input().split())
bar_weights = list(map(int, input().split()))
dp = [False] * (s + 1)
dp[0] = True
for i in range(1, n + 1):
    for w in range(s, 0, -1):
        if w >= bar_weights[i - 1] and dp[w - bar_weights[i - 1]]:
            dp[w] = True
max_weight = max(list(set([w if can_put else 0 for w, can_put in enumerate(dp)])))
print(max_weight)
