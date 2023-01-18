class FenwickTree3D:
    def __init__(self, n):
        self.n = n
        self.graph = [[[0] * n for _ in range(n)] for _ in range(n)]
        self.graph_sum = [[[0] * n for _ in range(n)] for _ in range(n)]

    def __getitem__(self, item):
        return self.graph[item[0]][item[1]][item[2]]

    def prefix_sum(self, p):
        x, y, z = p
        res = 0
        while x >= 0:
            y = p[1]
            while y >= 0:
                z = p[2]
                while z >= 0:
                    res += self.graph_sum[x][y][z]
                    z = (z & (z + 1)) - 1
                y = (y & (y + 1)) - 1
            x = (x & (x + 1)) - 1
        return res

    def calculate_stars(self, i, j):
        return (
            self.prefix_sum(j)
            - self.prefix_sum((j[0], j[1], i[2] - 1))
            - self.prefix_sum((j[0], i[1] - 1, j[2]))
            + self.prefix_sum((j[0], i[1] - 1, i[2] - 1))
            - self.prefix_sum((i[0] - 1, j[1], j[2]))
            + self.prefix_sum((i[0] - 1, j[1], i[2] - 1))
            + self.prefix_sum((i[0] - 1, i[1] - 1, j[2]))
            - self.prefix_sum((i[0] - 1, i[1] - 1, i[2] - 1))
        )

    def __setitem__(self, key, value):
        prev_val = self.graph[key[0]][key[1]][key[2]]
        self.graph[key[0]][key[1]][key[2]] = value
        x, y, z = key
        while x < self.n:
            y = key[1]
            while y < self.n:
                z = key[2]
                while z < self.n:
                    self.graph_sum[x][y][z] += value - prev_val
                    z = z | (z + 1)
                y = y | (y + 1)
            x = x | (x + 1)


n = int(input())
t = FenwickTree3D(n)
events = [0]
while events[0] != 3:
    events = list(map(int, input().split()))
    if events[0] == 1:
        x, y, z, k = events[1:]
        t[x, y, z] += k
    elif events[0] == 2:
        print(
            t.calculate_stars(
                (events[1], events[2], events[3]), (events[4], events[5], events[6])
            )
        )
