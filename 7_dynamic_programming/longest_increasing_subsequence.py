n = int(input())
arr = list(map(int, input().split()))
length, previous = [1 for _ in range(n)], [-1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and length[j] >= length[i]:
            length[i] = length[j] + 1
            previous[i] = j
last_element = length.index(max(length))
seq = []
while last_element != -1:
    seq.append(arr[last_element])
    last_element = previous[last_element]
seq.reverse()
print(max(length))
print(*seq)
