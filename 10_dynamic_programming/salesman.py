n = int(input())
paths_between_cities = [[int(i) for i in input().split()] for _ in range(n)]
arr, nums = [[10**7] * n for _ in range(1 << n)], [
    ["STOP"] * n for _ in range(1 << n)
]
order = []
for one in range(n):
    arr[1 << one][one] = 0
for m in range(1, 1 << n):
    for lst in range(n):
        if arr[m][lst] == 10**7:
            continue
        for nxt in range(n):
            if m & (1 << nxt) != 0:
                continue
            if arr[m | (1 << nxt)][nxt] > arr[m][lst] + paths_between_cities[lst][nxt]:
                nums[m | (1 << nxt)][nxt] = (m, lst)
                arr[m | (1 << nxt)][nxt] = arr[m][lst] + paths_between_cities[lst][nxt]
smallest_dist, last = arr[(1 << n) - 1][0], 0
for i, dist in enumerate(arr[(1 << n) - 1]):
    if dist < smallest_dist:
        smallest_dist = dist
        last = i
current = ((1 << n) - 1, last)
while current != "STOP":
    order.append(current[1] + 1)
    current = nums[current[0]][current[1]]
print(smallest_dist)
print(" ".join([str(i) for i in reversed(order)]))
