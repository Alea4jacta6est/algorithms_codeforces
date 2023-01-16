class Queue:
    def __init__(self):
        self.queue = []

    def add(self, x):
        self.queue.append(x)

    def retrieve(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return


n = int(input())
q = Queue()
for i in range(n):
    operation = input().split()
    if operation[0] == "+":
        q.add(int(operation[1]))
    elif operation[0] == "-":
        result = q.retrieve()
        if result:
            print(result)
