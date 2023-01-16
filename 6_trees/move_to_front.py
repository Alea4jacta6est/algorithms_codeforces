import random


def update_subtree(root):
    root.size = 1
    if root.left is not None:
        root.size += root.left.size
    if root.right is not None:
        root.size += root.right.size


def split_tree(root, key):
    if root is None:
        return None, None
    r = root.left.size if root.left is not None else 0
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
    elif left.pr > right.pr:
        left.right = merge(left.right, right)
        update_subtree(left)
        return left
    else:
        right.left = merge(left, right.left)
        update_subtree(right)
        return right


class Node:
    def __init__(self, p):
        self.left = None
        self.right = None
        self.pr = random.getrandbits(64)
        self.size = 1
        self.p = p


def find(root, pos):
    if root is None:
        return False
    if root.size == pos:
        return True
    elif pos < root.size:
        return find(root.left, pos)
    else:
        return find(root.right, pos)


def insert(root, pos, p):
    new_node = Node(p)
    if root is None:
        return new_node
    left, right = split_tree(root, pos)
    root = merge(left, new_node)
    root = merge(root, right)
    return root


def ordering(root, res=[]):
    if root is not None:
        ordering(root.left, res)
        res.append(root)
        ordering(root.right, res)
    return res


def move_to_front(root, i, j):
    l1, r1 = split_tree(root, j)
    l2, r2 = split_tree(l1, i - 1)
    return merge(r2, merge(l2, r1))


root = None
n, m = map(int, input().split())
for i in range(1, n + 1):
    root = insert(root, i, i)
for _ in range(m):
    l, r = [int(i) for i in input().split()]
    root = move_to_front(root, l - 1, r - 1)
print(" ".join([str(i.p) for i in ordering(root)]))
