def get_timbers_sum(timbers, k):
    max_timber = sum(timbers) // k

    def timbers_diff(timber_length):
        return k - sum(timber // timber_length for timber in timbers)

    left, right = 0, max_timber + 1
    new_timber = (right + left) // 2
    while new_timber != left:
        if timbers_diff(new_timber) > 0:
            right = new_timber
        elif timbers_diff(new_timber) <= 0:
            left = new_timber
        new_timber = (right + left) // 2
    return new_timber


n, k = [int(i) for i in input().split()]
timbers = [int(input()) for _ in range(n)]
print(get_timbers_sum(timbers, k))

# 4 11
# 802
# 743
# 457
# 539
