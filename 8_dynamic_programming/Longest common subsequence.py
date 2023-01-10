"""
3
1 2 3
4
2 3 1 5
"""
from sys import stdin


def longest_common_subsequence(s1, s2):
    seq = {}
    m, n, cnt = len(s1), len(s2), 0
    d = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                d[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i - 1][j], d[i][j - 1])
    print(seq)
    target_seq = [seq[k] for k in seq if len(seq[k]) == d[m][n]][0]
    return " ".join(target_seq), d[m][n]


# inputs = [item.replace(" ", "").replace("\n", "") for item in stdin.readlines()]
# seq, length = longest_common_subsequence(inputs[1], inputs[3])
# print(length)
# print(seq)
print(longest_common_subsequence([1, 2, 3], [2, 3, 1, 5]))
