from sys import stdin, stdout


def sieve_eratosthenes(n):
    prime_state, p = [False, False], 2
    prime_state.extend([True for i in range(p, n + 1)])
    while p * p <= n:
        if prime_state[p]:
            for i in range(p * p, n + 1, p):
                prime_state[i] = False
        p += 1
    return prime_state


def print(s):
    stdout.write(str(s) + "\n")


numbers = [int(item) for item in stdin.readlines()[1:]]
results = sieve_eratosthenes(max(numbers))
for num in numbers:
    if results[num]:
        print("YES")
    else:
        print("NO")
