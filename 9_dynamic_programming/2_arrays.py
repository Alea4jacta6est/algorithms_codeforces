from collections import defaultdict


test_cases = int(input())
for _ in range(test_cases):
    n, t = list(map(int, input().split()))
    a = list(map(int, input().split()))
    white, black = set(), set()
    black_number, white_number = defaultdict(int), defaultdict(int)
    p_s = [0] * n
    for i in range(n):
        cmp = t - a[i]
        if cmp == a[i]:
            if black_number[cmp] > white_number[cmp]:
                white_number[cmp] += 1
                p_s[i] = 1
            else:
                black_number[cmp] += 1
        else:
            if cmp in black or a[i] in white:
                p_s[i] = 1
                white.add(a[i])
            else:
                black.add(a[i])
    print(" ".join(map(str, p_s)))
