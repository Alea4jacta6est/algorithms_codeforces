t = int(input())
for _ in range(t):
    n = int(input())
    max_chairs = 4 * n
    final = []
    for k in range(2, max_chairs // 2 + 1, 2):
        arr = []
        for i in range(k, max_chairs, 2):
            flag = True
            for e in arr:
                if i % e == 0:
                    flag = False
            if flag:
                arr.append(i)
        if len(arr) >= n:
            final = arr[:n]
    print(" ".join([str(i) for i in final]))
