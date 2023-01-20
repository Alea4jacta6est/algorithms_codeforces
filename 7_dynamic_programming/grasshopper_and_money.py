class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.stree_size = 1


def min_vertex(root):
    if root is None or root.left is None:
        return root
    return min_vertex(root.left)


def max_vertex(root):
    if root is None or root.right is None:
        return root
    return max_vertex(root.right)


def insert_vertex(root, key):
    if root is None:
        return Node(key)
    elif key < root.key:
        root.left = insert_vertex(root.left, key)
    else:
        root.right = insert_vertex(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    root.stree_size = 1 + get_stree_size(root.left) + get_stree_size(root.right)
    balance = get_balance(root)
    if balance > 1 and key < root.left.key:
        return right_rotation(root)
    if balance < -1 and key > root.right.key:
        return left_rotation(root)
    if balance > 1 and key > root.left.key:
        root.left = left_rotation(root.left)
        return right_rotation(root)
    if balance < -1 and key < root.right.key:
        root.right = right_rotation(root.right)
        return left_rotation(root)

    return root


def delete_vertex(root, key):
    if root is None:
        return None
    elif key < root.key:
        root.left = delete_vertex(root.left, key)
    elif key > root.key:
        root.right = delete_vertex(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_vertex(root.right)
        root.key = temp.key
        root.right = delete_vertex(root.right, temp.key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    root.stree_size = 1 + get_stree_size(root.left) + get_stree_size(root.right)
    balance = get_balance(root)
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotation(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotation(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotation(root.left)
        return right_rotation(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotation(root.right)
        return left_rotation(root)
    return root


def left_rotation(z):
    y = z.right
    if y is not None:
        t2 = y.left
        y.left = z
    else:
        t2 = None
    z.right = t2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    z.stree_size = 1 + get_stree_size(z.left) + get_stree_size(z.right)
    if y is not None:
        y.height = 1 + max(get_height(y.left), get_height(y.right))
        y.stree_size = 1 + get_stree_size(y.left) + get_stree_size(y.right)
    return y


def right_rotation(z):
    y = z.left
    if y is not None:
        t3 = y.right
        y.right = z
    else:
        t3 = None
    z.left = t3
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    z.stree_size = 1 + get_stree_size(z.left) + get_stree_size(z.right)
    if y is not None:
        y.height = 1 + max(get_height(y.left), get_height(y.right))
        y.stree_size = 1 + get_stree_size(y.left) + get_stree_size(y.right)
    return y


def get_balance(root):
    if not root:
        return 0
    return get_height(root.left) - get_height(root.right)


def get_height(root):
    if not root:
        return 0
    return root.height


def get_stree_size(root):
    if not root:
        return 0
    return root.stree_size


def get_right_count(root):
    if root.right is None:
        return 0
    return root.right.stree_size


tree = None
n, k = map(int, input().split())
coins = [0] + list(map(int, input().split())) + [0]
dp = [0] * n
dp[0] = 0
f = [0] * n
for i in range(1, n):
    tree = insert_vertex(tree, (dp[i - 1], i - 1))
    if i - k > 0:
        tree = delete_vertex(tree, (dp[i - k - 1], i - k - 1))
    m = max_vertex(tree).key
    dp[i] = m[0] + coins[i]
    f[i] = m[1]
path = [len(coins) - 1]
while path[-1] != 0:
    path.append(f[path[-1]])
print(dp[n - 1])
print(len(path) - 1)
print(" ".join([str(a + 1) for a in reversed(path)]))
