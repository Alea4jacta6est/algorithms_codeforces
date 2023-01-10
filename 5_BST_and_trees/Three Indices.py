from sys import stdin

# a = [[int(num) for num in item.split()] for i, item in enumerate(stdin.readlines()[1:])]
n = int(stdin.readline())
a = [[int(num) for num in stdin.readline().split()] for i in range(n * 2)]
for p in a:
    if len(p) > 1:
        for i in range(len(p)):
            try:
                if p[i] > p[i - 1] and p[i] > p[i + 1]:
                    print("YES")
                    print(i, i + 1, i + 2)
                    break
            except:
                break
        else:
            print("NO")

"""3
4
2 1 4 3
6
4 6 1 2 5 3
5
5 3 1 2 4"""
