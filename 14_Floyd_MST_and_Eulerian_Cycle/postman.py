from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)
def dfs(vertex, links, streets):
    for i in links[vertex]:
        if not i.d:
            i.d = True
            to = i.to if vertex == i.from_ else i.from_
            dfs(to, links, streets)
    streets.append(vertex)


class Link:
    def __init__(self, from_, to, w):
        self.w = w
        self.from_ = from_
        self.to = to
        self.d = False


n = int(input())
graph = [[int(i) for i in item.split()] for item in stdin.readlines()]
links, streets, arr = {i: [] for i, item in enumerate(graph)}, [], []
counter = 0
for i, arr in enumerate(graph):
    if arr[0] % 2 != 0:
        counter += 1
        arr.append(i)
    for j in range(1, len(arr), 2):
        e = Link(i, arr[j] - 1, arr[j + 1])
        if arr[j] - 1 not in links:
            links[arr[j] - 1] = []
        if i < arr[j] - 1:
            links[i].append(e)
            links[arr[j] - 1].append(e)

if counter % 2 == 1:
    print(-1)
    exit(0)
    
if counter == 2:
    for i in links[arr[0]]:
        if i.f == arr[0] and i.t == arr[1]:
            streets.append(arr[0])
            i.d = True
            dfs(arr[1], links, streets)
            break
else:
    dfs(0, links, streets)

print(len(streets) - 1)
for i in streets:
    print(i + 1, end=" ")
