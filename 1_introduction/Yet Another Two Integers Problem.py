def get_min_operations(a, b):
    steps, k = 0, 10
    if a == b:
        return steps
    elif a < b:
        diff = b - a
    else:
        diff = a - b
    while diff > k:
        if diff % k == 0:
            return diff // 10
        else:
            return diff // 10 + 1


if __name__ == "__main__":
    t = int(input())
    while t > 0:
        a, b = map(int, input().split())
        print((abs(a - b) + 9) // 10)
        t -= 1
