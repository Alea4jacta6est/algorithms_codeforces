# 7
# 0 100
# 0 10
# 1
# 0 5
# 0 30
# 0 50
# 1
from sys import stdin

data = []
n = int(stdin.readline())
inputs = [stdin.readline().strip() for i in range(n)]
for line in inputs:
    if line.startswith("0"):
        digit = int(line.split()[1])
        data.append(digit)
    if line == "1":
        print(max(data))
        data.remove(max(data))
