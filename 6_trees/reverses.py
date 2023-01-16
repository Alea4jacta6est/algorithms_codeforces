"""5 3
2 4
3 5
2 2
    """
"""10 4
1 9
9 9
8 7
3 5
    """
from sys import stdin
import random


def update_subtree(root):
    root.subtree_size = 1
    if root.left is not None:
        root.subtree_size += root.left.subtree_size
    if root.right is not None:
        root.subtree_size += root.right.subtree_size


class Node:
    def __init__(self, p):
        self.left = None
        self.right = None
        self.pr = random.getrandbits(46)
        self.subtree_size = 1
        self.p = p
        self.to_rotate = False


def split_tree(root, key):
    if root is None:
        return None, None
    push(root)
    r = root.left.subtree_size if root.left is not None else 0
    if key < r:
        left, root.left = split_tree(root.left, key)
        update_subtree(root)
        return left, root
    else:
        root.right, right = split_tree(root.right, key - r - 1)
        update_subtree(root)
        return root, right


def merge(left, right):
    if left is None:
        return right
    elif right is None:
        return left
    push(left)
    push(right)
    if left.pr > right.pr:
        left.right = merge(left.right, right)
        update_subtree(left)
        return left
    else:
        right.left = merge(left, right.left)
        update_subtree(right)
        return right


def find(root, key):
    if root is None:
        return False
    if root.subtree_size == key:
        return True
    elif key < root.subtree_size:
        return find(root.left, key)
    else:
        return find(root.right, key)


def insert(root, key, p):
    new_node = Node(p)
    if root is None:
        return new_node
    left, right = split_tree(root, key - 1)
    root = merge(left, new_node)
    root = merge(root, right)
    return root


def rotate(root, i, j):
    l1, r1 = split_tree(root, j)
    l2, r2 = split_tree(l1, i - 1)
    r2.to_rotate = True
    return merge(merge(l2, r2), r1)


def push(root):
    if root.to_rotate:
        left = root.left
        root.left = root.right
        root.right = left
        root.to_rotate = False
        if root.left is not None:
            root.left.to_rotate = root.left.to_rotate is not True
        if root.right is not None:
            root.right.to_rotate = root.right.to_rotate is not True


def ordering(root):
    global result
    if root is not None:
        push(root)
        ordering(root.left)
        result.append(str(root.p))
        ordering(root.right)


result, root = [], None
n, m = (int(i) for i in stdin.readline().split())
inputs = stdin.readlines()
ops = [[int(it) for it in line.split()] for line in inputs]
for i in range(1, n + 1):
    root = insert(root, i, i)
for l, r in ops:
    root = rotate(root, l - 1, r - 1)
ordering(root)
print(" ".join(result))
