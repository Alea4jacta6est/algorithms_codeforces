n = int(input())
prev_table = {
    0: [4, 6],
    1: [8, 6],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}
nums = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    if i != 8 and i != 0:
        nums[1][i] = 1
for i in range(2, n + 1):
    for d in range(10):
        if d != 5:
            for prev_d in prev_table[d]:
                nums[i][d] += nums[i - 1][prev_d]
print(sum(nums[n]) % 10**9)
