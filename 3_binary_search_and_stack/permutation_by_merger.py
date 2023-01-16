# 5
# 2
# 1 1 2 2
# 4
# 1 3 1 4 3 4 2 2
# 5
# 1 2 1 2 3 4 3 5 4 5
# 3
# 1 2 3 1 2 3
# 4
# 2 3 2 4 1 3 4 1
def get_unique_elements(seq):
    unique = []
    for item in seq:
        if item not in unique:
            unique.append(item)
    return unique


n = int(input())
for _ in range(n):
    seq_num = input()
    seq = " ".join(get_unique_elements(input().split()))
    print(seq)
