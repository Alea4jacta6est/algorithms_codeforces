from collections import deque


n = int(input())
queue = deque()
qt = deque()
res = []
len_1, len_2 = 0, 0
for i in range(n):
    t1 = input().split()
    if "-" in t1:
        res.append(queue.popleft())
        len_1 -= 1
    elif "+" in t1:
        qt.append(t1[-1])
        len_2 += 1
    else:
        qt.appendleft(t1[-1])
        len_2 += 1
    if len_1 < len_2:
        queue.append(qt.popleft())
        len_2 -= 1
        len_1 += 1
print(*res, sep="\n")
