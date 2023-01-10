"""5 3
2 4
3 5
2 2
    """
"""10 4
1 9
9 9
8 7
3 5
    """
from sys import stdin

n, m = (int(i) for i in stdin.readline().split())
a = [str(i) for i in range(1, n + 1)]
inputs = [stdin.readline().split() for _ in range(m)]
for i, nums in enumerate(inputs):
    num_1, num_2 = nums[0], nums[1]
    k, j = a.index(num_1), a.index(num_2)
    a[k], a[j] = a[j], a[k]
print(" ".join(a))
