"""4
1
2
3
4"""
from sys import stdin

inputs = [int(item) for item in stdin.readlines()][1:]
for i, inp in enumerate(inputs):
    print(int((1 + inp) / 2))
