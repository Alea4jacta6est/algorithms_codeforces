data = "4 6 11 11 15 18 20"
data = "10 10 10 11"
data = "1 1 1000000000"
# a + b > c a + c > b b + c > a


def get_triangle(seq):
    if len(seq) < 3:
        return -1
    else:
        sorted_seq = sorted(seq)
        try:
            for i, a in enumerate(sorted_seq):
                if not (
                    sorted_seq[i] + sorted_seq[i + 1] > sorted_seq[i + 2]
                    and sorted_seq[i] + sorted_seq[i + 2] > sorted_seq[i + 1]
                    and sorted_seq[i + 1] + sorted_seq[i + 2] > sorted_seq[i]
                ):

                    return [seq.index(item, i) + 1 for item in sorted_seq[i : i + 3]]
        except IndexError:
            return -1


seq = [int(item) for item in data.split()]
print(get_triangle(seq))
