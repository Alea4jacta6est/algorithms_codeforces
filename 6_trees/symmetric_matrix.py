t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    output = "NO"
    for _ in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if b == c:
            output = "YES"
    if m % 2 == 1:
        output = "NO"
    print(output)
