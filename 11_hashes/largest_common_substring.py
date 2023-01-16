from sys import hash_info


def get_prefix_hashes(s, r):
    prefix_hashes = [0] * len(s)
    prefix_hashes[0] = s[0] % r
    for i in range(1, len(s)):
        prefix_hashes[i] = (prefix_hashes[i - 1] * 257 + s[i]) % r
    return prefix_hashes


def substring_hash(i, j, prefix_hash, s):
    return (prefix_hash[j] - (prefix_hash[i] - s[i]) * pows[j - i]) % r


s1 = [ord(i) for i in input()]
s2 = [ord(i) for i in input()]
min_seq_length = min(len(s1), len(s2))
r = hash_info.modulus
pows = [1] * min_seq_length
for i in range(1, min_seq_length):
    pows[i] = pows[i - 1] * 257 % r

prefix_hash_1 = get_prefix_hashes(s1, r)
prefix_hash_2 = get_prefix_hashes(s2, r)
left = 0
right = min_seq_length + 1
while left < right - 1:
    current = (left + right) // 2
    substrings_1 = set(
        substring_hash(i, i + current - 1, prefix_hash_1, s1)
        for i in range(len(s1) - current + 1)
    )
    substrings_2 = set(
        substring_hash(i, i + current - 1, prefix_hash_2, s2)
        for i in range(len(s2) - current + 1)
    )
    if len(substrings_1.intersection(substrings_2)) != 0:
        left = current
    else:
        right = current
print(left)

# SLOW BUT GOOD


def largest_common_substring(seq1, seq2):
    substrings = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]
    longest = 0
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                current = substrings[i][j] + 1
                substrings[i + 1][j + 1] = current
                if current > longest:
                    longest = current
    return longest


# s_0 = input()
# s_1 = input()
# print(largest_common_substring(s_0, s_1))
