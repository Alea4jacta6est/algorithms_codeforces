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


def count_storage(ops):
    stack_storage, size = 0, 0
    for operation in ops:
        if operation[0] == "1":
            size += 1
        elif operation[0] == "2":
            size -= 1

        if size > stack_storage:
            stack_storage = size
    return stack_storage


num_ops = int(input())
ops = [input().split() for _ in range(num_ops)]
stack_storage = count_storage(ops)
stack = Stack(stack_storage)
for operation in ops:
    if operation[0] == "1":
        stack.push(operation[1])
    else:
        print(stack.pop())
