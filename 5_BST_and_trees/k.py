"""11
1 5
1 3
1 7
0 1
0 2
0 3
-1 5
1 10
0 1
0 2
0 3"""
from sys import stdin

data, inputs = [], [item.replace("\n", "").split() for item in stdin.readlines()[1:]]
for num, digit in inputs:
    if num in ("1",):
        data.append(int(digit))
    if num in ("0",):
        data.sort(reverse=True)
        print(data[int(digit) - 1])
    if num in ("-1",):
        data.remove(int(digit))
