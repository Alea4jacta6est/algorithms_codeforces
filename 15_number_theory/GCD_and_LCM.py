from sys import stdin
import math

# :P
n, m = (int(i) for i in stdin.readline().split())
print(" ".join(map(str, [math.gcd(n, m), math.lcm(n, m)])))
