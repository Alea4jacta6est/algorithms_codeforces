from sys import stdin


def is_heap(array, n):
    for i in range(n // 2):
        if ((2 * i + 1) < n and (array[i] > array[2 * i + 1])) or (
            (2 * i + 2) < n and (array[i] > array[2 * i + 2])
        ):
            return False
    return True


n = int(stdin.readline())
array = [int(i) for i in input().split()]
if is_heap(array, n):
    print("YES")
else:
    print("NO")
