from sys import stdin


def find_prime(n):
    factors, i = [], 2
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n, i = n / i, i - 1
        i += 1
    return factors


n = int(stdin.readline())
factors = find_prime(n)
print(" ".join(map(str, factors)))
