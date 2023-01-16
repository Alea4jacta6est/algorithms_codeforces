t, r = [int(i) for i in input().split()]
sequence = [ord(i) for i in input()]
m = int(input())
substrings = [[int(i) for i in input().split()] for _ in range(m)]
sub_hashes = []
hashes = [0] * len(sequence)
hashes[0] = sequence[0] % r
for i in range(1, len(sequence)):
    hashes[i] = (hashes[i - 1] * t + sequence[i]) % r
pows = [1] * 100000
for i in range(1, 100000):
    pows[i] = pows[i - 1] * t % r
for a, b in substrings:
    new_hash = (hashes[b] - (hashes[a] - sequence[a]) * pows[b - a]) % r
    sub_hashes.append(new_hash)
for hash in sub_hashes:
    print(hash)
