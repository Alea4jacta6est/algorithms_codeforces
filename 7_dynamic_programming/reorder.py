t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    if sum(a) == m:
        print("YES")
    else:
        print("NO")
