from sys import stdin


def extended_version_of_gcd(n, m):
    if n == 0:
        return 0, 1
    x1, y1 = extended_version_of_gcd(m % n, n)
    x = y1 - (m // n) * x1
    y = x1
    return x, y


inputs = [[int(_) for _ in item.split()] for item in stdin.readlines()[1:]]
for n, m in inputs:
    x, y = extended_version_of_gcd(n, m)
    print(x, y)
