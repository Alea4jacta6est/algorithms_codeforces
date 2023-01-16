# n, k = map(int, input().split())
# coins = list(map(int, input().split()))

# from typing import Optional


# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None
#         self.height = 1
#         self.subtree_size = 1


# def insert_node(root, key):
#     if root is None:
#         return TreeNode(key)
#     elif key < root.key:
#         root.left = insert_node(root.left, key)
#     else:
#         root.right = insert_node(root.right, key)

#     root.height = 1 + max(get_height(root.left), get_height(root.right))
#     root.subtree_size = 1 + get_subtree_size(root.left) + get_subtree_size(root.right)
#     balance = get_balance(root)
#     if balance > 1 and key < root.left.key:
#         return right_rotate(root)
#     if balance < -1 and key > root.right.key:
#         return left_rotate(root)
#     if balance > 1 and key > root.left.key:
#         root.left = left_rotate(root.left)
#         return right_rotate(root)
#     if balance < -1 and key < root.right.key:
#         root.right = right_rotate(root.right)
#         return left_rotate(root)
#     return root


# def delete_node(root, key):
#     if root is None:
#         return None
#     elif key < root.key:
#         root.left = delete_node(root.left, key)
#     elif key > root.key:
#         root.right = delete_node(root.right, key)
#     else:
#         if root.left is None:
#             return root.right
#         elif root.right is None:
#             return root.left
#         temp = min_node(root.right)
#         root.key = temp.key
#         root.right = delete_node(root.right, temp.key)

#     root.height = 1 + max(get_height(root.left), get_height(root.right))
#     root.subtree_size = 1 + get_subtree_size(root.left) + get_subtree_size(root.right)
#     balance = get_balance(root)
#     if balance > 1 and get_balance(root.left) >= 0:
#         return right_rotate(root)
#     if balance < -1 and get_balance(root.right) <= 0:
#         return left_rotate(root)
#     if balance > 1 and get_balance(root.left) < 0:
#         root.left = left_rotate(root.left)
#         return right_rotate(root)
#     if balance < -1 and get_balance(root.right) > 0:
#         root.right = right_rotate(root.right)
#         return left_rotate(root)
#     return root


# def min_node(root):
#     if root is None or root.left is None:
#         return root
#     return min_node(root.left)


# def max_node(root) -> Optional[TreeNode]:
#     if root is None or root.right is None:
#         return root
#     return max_node(root.right)


# def left_rotate(z):
#     y = z.right
#     if y is not None:
#         t2 = y.left
#         y.left = z
#     else:
#         t2 = None
#     z.right = t2
#     z.height = 1 + max(get_height(z.left), get_height(z.right))
#     z.subtree_size = 1 + get_subtree_size(z.left) + get_subtree_size(z.right)
#     if y is not None:
#         y.height = 1 + max(get_height(y.left), get_height(y.right))
#         y.subtree_size = 1 + get_subtree_size(y.left) + get_subtree_size(y.right)
#     return y


# def right_rotate(z):
#     y = z.left
#     if y is not None:
#         t3 = y.right
#         y.right = z
#     else:
#         t3 = None
#     z.left = t3
#     z.height = 1 + max(get_height(z.left), get_height(z.right))
#     z.subtree_size = 1 + get_subtree_size(z.left) + get_subtree_size(z.right)
#     if y is not None:
#         y.height = 1 + max(get_height(y.left), get_height(y.right))
#         y.subtree_size = 1 + get_subtree_size(y.left) + get_subtree_size(y.right)
#     return y


# def get_height(root):
#     if not root:
#         return 0
#     return root.height


# def get_subtree_size(root):
#     if not root:
#         return 0
#     return root.subtree_size


# def get_right_count(root):
#     if root is None:
#         raise ValueError("Root cannot be None")
#     if root.right is None:
#         return 0
#     return root.right.subtree_size


# def get_balance(root):
#     if not root:
#         return 0
#     return get_height(root.left) - get_height(root.right)


# if __name__ == "__main__":
#     avl = None
#     n, k = map(int, input().split())
#     coins = [0] + list(map(int, input().split())) + [0]
#     dp = [0] * n
#     dp[0] = 0
#     _from = [0] * n
#     for i in range(1, n):
#         avl = insert_node(avl, (dp[i - 1], i - 1))
#         if i - k > 0:
#             avl = delete_node(avl, (dp[i - k - 1], i - k - 1))
#         mx = max_node(avl).key
#         dp[i] = mx[0] + coins[i]
#         _from[i] = mx[1]
#     path = [len(coins) - 1]
#     while path[-1] != 0:
#         path.append(_from[path[-1]])
#     print(dp[n - 1])
#     print(len(path) - 1)
#     print(" ".join([str(a + 1) for a in reversed(path)]))
n, k = map(int, input().split())
coins = list(map(int, input().split()))

# Initialize the array dp to store the maximum number of coins that can be obtained
# by starting at cell i and jumping j cells
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

# Initialize the array path to store the optimal path
path = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

# Base case: starting at cell 1, the grasshopper can only jump 1 cell and obtain the
# number of coins from that cell
for j in range(1, k + 1):
    dp[1][j] = coins[0]
    path[1][j] = [1, 1 + j]

# Iterate through the cells and the number of jumps
for i in range(2, n + 1):
    for j in range(1, k + 1):
        max_coins = 0
        max_path = []
        # Iterate through the number of cells that can be jumped
        for l in range(1, j + 1):
            if i - l < 1:
                continue
            # Check if the current number of coins is greater than the maximum number
            # of coins obtained so far
            if dp[i - l][j] + coins[i - 2] > max_coins:
                max_coins = dp[i - l][j] + coins[i - 2]
                max_path = path[i - l][j] + [i]
        dp[i][j] = max_coins
        path[i][j] = max_path

# Find the maximum number of coins obtained and the optimal path
max_coins = 0
opt_path = []
jumps = 0
for j in range(1, k + 1):
    if dp[n][j] > max_coins:
        max_coins = dp[n][j]
        opt_path = path[n][j]
        jumps = j

print(max_coins)
print(jumps)
print(*opt_path)
