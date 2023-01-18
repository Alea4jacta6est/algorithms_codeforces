from sys import stdin

n = int(input())
counter_1, counter_2 = [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    for j, v in enumerate(stdin.readline().split()):
        if v == "1":
            counter_1[i] += 1
            counter_2[j] += 1
sink_nodes, sources = [], []
for i in range(n):
    if counter_1[i] == 0:
        sink_nodes.append(str(i + 1))
    if counter_2[i] == 0:
        sources.append(str(i + 1))
print(len(sources), end=" ")
print(" ".join(sources))
print(len(sink_nodes), end=" ")
print(" ".join(sink_nodes))
