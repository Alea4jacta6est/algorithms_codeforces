class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * n
        self.sum_subset = [0] * n

    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)

    def prefix_sum(self, p):
        final_sum = 0
        while p >= 0:
            final_sum += self.sum_subset[p]
            p = (p & (p + 1)) - 1
        return final_sum

    def set_by_index(self, i: int, value: int):
        old_value = self.arr[i]
        self.arr[i] = value
        current = i
        while current < self.n:
            self.sum_subset[current] += value - old_value
            current = current | (current + 1)


n, k = map(int, input().split())
tree = FenwickTree(n)
for i in range(k):
    query, e1, e2 = input().split()
    e1, e2 = int(e1), int(e2)
    if query == "Q":
        print(tree.range_sum(e1 - 1, e2 - 1))
    elif query == "A":
        tree.set_by_index(e1 - 1, e2)
