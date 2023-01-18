n = int(input())
edges_number = 0
for _ in range(n):
    for edge in input().split():
        if edge == "1":
            edges_number += 1
print(edges_number // 2)
