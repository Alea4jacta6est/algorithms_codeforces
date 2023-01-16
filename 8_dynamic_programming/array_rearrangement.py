t = int(input())
for _ in range(t):
    inputs = ""
    while inputs == "":
        inputs = input().strip()
    n, x = list(map(int, inputs.split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rearrange = True
    for ai, bi in zip(a, reversed(b)):
        if ai + bi > x:
            rearrange = False
            break
    if rearrange:
        print("Yes")
    else:
        print("No")
