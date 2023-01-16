import sys

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dp = [[0] * len(b) for _ in range(len(a))]
_from = [[None] * len(b) for _ in range(len(a))]


def get_dp(i, j):
    if i < 0 or j < 0:
        return 0
    else:
        return dp[i][j]


for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            dp[i][j] = get_dp(i - 1, j - 1) + 1
        max_dp_i = max(
            (get_dp(i - 1, j), (i - 1, j)),
            (get_dp(i, j - 1), (i, j - 1)),
            (get_dp(i, j), (i - 1, j - 1)),
            key=lambda x: x[0],
        )
        dp[i][j] = max_dp_i[0]
        _from[i][j] = max_dp_i[1]

longest_common_subs = []
cur = (len(a) - 1, len(b) - 1)
while cur[0] != -1 and cur[1] != -1:
    nxt = _from[cur[0]][cur[1]]
    if nxt == (cur[0] - 1, cur[1] - 1):
        longest_common_subs.append(a[cur[0]])
    cur = nxt

print(len(longest_common_subs))
for subs in reversed(longest_common_subs):
    sys.stdout.write(str(subs) + " ")
