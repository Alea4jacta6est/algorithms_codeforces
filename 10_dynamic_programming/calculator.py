n = int(input())
arr, nums = [0 for _ in range(n + 1)], [i - 1 for i in range(n + 1)]
for i in range(2, n + 1):
    arr[i] = arr[i - 1] + 1
    if i % 2 == 0 and arr[i // 2] + 1 < arr[i]:
        arr[i] = arr[i // 2] + 1
        nums[i] = i // 2
    if i % 3 == 0 and arr[i // 3] + 1 < arr[i]:
        arr[i] = arr[i // 3] + 1
        nums[i] = i // 3
paths = [n]
while paths[-1] != 1:
    paths.append(nums[paths[-1]])
print(arr[n])
print(" ".join([str(i) for i in reversed(paths)]))
