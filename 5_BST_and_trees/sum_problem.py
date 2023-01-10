"""6
+ 1
+ 3
+ 3
? 2 4
+ 1
? 2 4
"""
from sys import stdin, stdout
import bisect


def print(s):
    stdout.write(f"{s}\n")


inputs, s, y = [item.split() for item in stdin.readlines()[1:]], [], 0
for j, inp in enumerate(inputs):
    if inp[0] in ("?",):
        y = sum([i for i in s if i >= int(inp[1]) and i <= int(inp[2])])
        print(y)
    else:
        d = (int(inp[1]) + y) % 10**9 if inputs[j - 1][0] in ("?",) else int(inp[1])
        if d not in s:
            bisect.insort(s, d)
