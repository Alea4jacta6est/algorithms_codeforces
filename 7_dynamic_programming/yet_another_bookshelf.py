t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    first, last = None, None
    for i in range(n):
        if a[i] == 1:
            if first is None:
                first = i
            last = i
    m = (last - first + 1) - sum(a[first : last + 1])
    print(m)
