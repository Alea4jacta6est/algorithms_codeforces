from sys import stdin


def sieve_eratosthenes(m, n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[1], prime[0] = False, False
    return [str(p) for p in range(m, n + 1) if prime[p]]


def get_primes(a, b):
    nums = []
    for num in range(a, b + 1):
        if num in [0, 1]:
            continue
        else:
            for i in range(2, int(num / 2) + 1):
                if (num % i) == 0:
                    break
            else:
                nums.append(str(num))
    return nums


n, m = (int(i) for i in stdin.readline().split())
print(" ".join([i for i in sieve_eratosthenes(n, m)]))
