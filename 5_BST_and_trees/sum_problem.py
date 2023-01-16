"""6
+ 1
+ 3
+ 3
? 2 4
+ 1
? 2 4
"""
import random
from sys import stdin


def find_by_key(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    elif key < root.key:
        return find_by_key(root.left, key)
    else:
        return find_by_key(root.right, key)


def split_tree(root, key):
    if root is None:
        return None, None
    if key < root.key:
        left, root.left = split_tree(root.left, key)
        update_subtree(root)
        return left, root
    else:
        root.right, right = split_tree(root.right, key)
        update_subtree(root)
        return root, right


def merge(left, right):
    if left is None:
        return right
    elif right is None:
        return left
    elif left.pr > right.pr:
        left.right = merge(left.right, right)
        update_subtree(left)
        return left
    else:
        right.left = merge(left, right.left)
        update_subtree(right)
        return right


class Node:
    def __init__(self, key, pr):
        self.left = None
        self.right = None
        self.subtree_sum = key
        self.key = key
        self.pr = pr


def insert(root, key):
    if find_by_key(root, key):
        return root
    new_node = Node(key, random.getrandbits(64))
    if root is None:
        return new_node
    left, right = split_tree(root, key - 1)
    root = merge(left, new_node)
    return merge(root, right)


def update_subtree(root):
    root.subtree_sum = root.key
    if root.left is not None:
        root.subtree_sum += root.left.subtree_sum
    if root.right is not None:
        root.subtree_sum += root.right.subtree_sum


def get_sum(root, start, end):
    left_sub, right_sub = split_tree(root, start - 0.5)
    left, right = split_tree(right_sub, end + 0.5)
    if left is not None:
        result = left.subtree_sum
    else:
        result = 0
    right = merge(left, right)
    root = merge(left_sub, right)
    return root, result


ROOT, PREV_OPERATION, PREV_VALUE = None, None, 0
for operation in [line.split() for line in stdin.readlines()[1:]]:
    num = int(operation[1])
    if operation[0] == "+":
        if PREV_OPERATION is None or PREV_OPERATION == "+":
            ROOT = insert(ROOT, num)
        else:
            ROOT = insert(ROOT, (num + PREV_VALUE) % 10**9)
    else:
        num2 = int(operation[2])
        ROOT, PREV_VALUE = get_sum(ROOT, num, num2)
        print(PREV_VALUE)
    PREV_OPERATION = operation[0]
