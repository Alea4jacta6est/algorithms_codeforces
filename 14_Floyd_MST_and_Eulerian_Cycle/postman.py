import sys


def dfs(v, e, ans):
    for i in e[v]:
        if not i.d:
            i.d = True
            t = i.dir2 if v == i.dir1 else i.dir1
            dfs(t, e, ans)
    ans.append(v)


class Link:
    def __init__(self, dir1, dir2, w):
        self.dir1 = dir1
        self.dir2 = dir2
        self.w = w
        self.d = False


def run():
    n = int(input())
    edges = {}
    counter = 0
    bad_areas = []
    for v in range(n):
        arr = [int(x) for x in input().split()]
        number_of_streets = arr[0]
        if number_of_streets % 2 != 0:
            counter += 1
            bad_areas.append(v)
        if v not in edges:
            edges[v] = []
        for j in range(1, len(arr), 2):
            to_ = arr[j] - 1
            street_len = arr[j + 1]
            edge = Link(v, to_, street_len)
            if to_ not in edges:
                edges[to_] = []
            if v < to_:
                edges[v].append(edge)
                edges[to_].append(edge)
    if counter % 2 == 1:
        print(-1)
        exit(0)
    ans = []
    if counter == 2:
        number_of_streets, to_ = bad_areas[0], bad_areas[1]
        for v in edges[number_of_streets]:
            if v.dir1 == number_of_streets and v.dir2 == to_:
                ans.append(number_of_streets)
                v.d = True
                dfs(to_, edges, ans)
                break
    else:
        dfs(0, edges, ans)
    print(len(ans) - 1)
    for v in ans:
        print(v + 1, end=" ")


import threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=run)
main_thread.start()
main_thread.join()
