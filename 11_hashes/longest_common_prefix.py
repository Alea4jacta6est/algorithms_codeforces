from sys import hash_info, stdin


def wrapper():
    def get_prefix_hashes(s, r=hash_info.modulus):
        prefix_hashes = [0] * len(s)
        prefix_hashes[0] = s[0] % r
        for i in range(1, len(s)):
            prefix_hashes[i] = (prefix_hashes[i - 1] * 257 + s[i]) % r
        return prefix_hashes

    def substring_hash(i, j, prefix_hash, s):
        return (
            prefix_hash[j] - (prefix_hash[i] - s[i]) * pows[j - i]
        ) % hash_info.modulus

    def longest_common_prefix(a, b, prefix_hash, s):
        left = 0
        right = len(s) - max(a, b) + 1
        while left < right - 1:
            current = (left + right) // 2
            if substring_hash(a, a + current - 1, prefix_hash, s) == substring_hash(
                b, b + current - 1, prefix_hash, s
            ):
                left = current
            else:
                right = current
        return left

    s = list(map(ord, input()))
    m = int(input())
    indices = [map(int, item.split()) for item in stdin.readlines()]
    pows = [1] * len(s)
    for i in range(1, len(s)):
        pows[i] = pows[i - 1] * 257 % hash_info.modulus
    prefix_hash = get_prefix_hashes(s)
    for a, b in indices:
        print(longest_common_prefix(a, b, prefix_hash, s))


wrapper()
