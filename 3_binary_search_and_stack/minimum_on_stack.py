"""8
1 2
1 3
1 -3
3
2
3
2
3
"""


class Stack:
    def __init__(self, storage):
        self.storage = storage
        self.array = [0] * storage
        self.head = -1

    def push(self, x):
        if self.head >= self.storage - 1:
            raise Exception("Overflow")
        self.head += 1
        self.array[self.head] = x

    def pop(self):
        if self.head > -1:
            self.head -= 1
            return self.array[self.head + 1]
        else:
            raise Exception("Empty stack")

    def peek(self):
        return self.array[self.head]


class MinStack(Stack):
    def __init__(self, storage):
        self.stack = Stack(storage)
        self.min_stack = Stack(storage)

    def push(self, x):
        self.stack.push(x)
        if self.min_stack.head + 1 == 0:
            self.min_stack.push(x)
        else:
            self.min_stack.push(min(self.min_stack.peek(), x))

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        return self.min_stack.peek()


num_ops = int(input())
ops, output = [input().split() for _ in range(num_ops)], []
stack = MinStack(num_ops)
for operation in ops:
    if operation[0] == "1":
        stack.push(int(operation[1]))
    elif operation[0] == "2":
        stack.pop()
    elif operation[0] == "3":
        output.append(stack.get_min())
print("\n".join(str(num) for num in output))
