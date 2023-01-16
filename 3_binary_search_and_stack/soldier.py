from sys import stdin


def soldiers_can_see(n, seq_growth, directions):
    result, lstack, rstack = {}, [], []
    for i in range(n):
        left_h = seq_growth[i]
        if directions[i] == "L":
            result[i] = len(lstack)
        while len(lstack) and left_h > lstack[-1]:
            lstack.pop()
        lstack.append(left_h)
    for i in range(n - 1, -1, -1):
        right_h = seq_growth[i]
        if directions[i] == "R":
            result[i] = len(rstack)
        while len(rstack) and right_h > rstack[-1]:
            rstack.pop()
        rstack.append(right_h)
    return result


n = int(stdin.readline())
seq_growth = [int(i) for i in stdin.readline().strip().split()]
directions = stdin.readline().strip()
output = soldiers_can_see(n, seq_growth, directions)
for i in range(n):
    print(output[i], end=" ")
