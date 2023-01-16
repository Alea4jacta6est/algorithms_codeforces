t, r = [int(i) for i in input().split()]
sequence = [ord(i) for i in input()]
hashes = [0] * len(sequence)
hashes[0] = sequence[0] % r
for i in range(1, len(sequence)):
    hashes[i] = (hashes[i - 1] * t + sequence[i]) % r
for hash in hashes:
    print(hash)
