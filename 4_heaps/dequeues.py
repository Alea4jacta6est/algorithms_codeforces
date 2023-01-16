from collections import defaultdict

n = int(input())
inputs = [input().split() for _ in range(n)]
dequeues = defaultdict(list)
for action_item in inputs:
    if action_item[0] == "pushfront":
        dequeues[int(action_item[1])].insert(0, int(action_item[2]))
    elif action_item[0] == "pushback":
        dequeues[int(action_item[1])].append(int(action_item[2]))
    elif action_item[0] == "popfront":
        print(dequeues[int(action_item[1])].pop(0))
    elif action_item[0] == "popback":
        print(dequeues[int(action_item[1])].pop())
