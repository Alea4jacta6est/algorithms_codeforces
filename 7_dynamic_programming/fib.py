def multiplication(m1, m2, g, n, z):
    result = [[0] * n for _ in range(g)]
    for i in range(g):
        for j in range(n):
            result[i][j] = sum([m1[i][k] * m2[k][j] for k in range(z)]) % d
    return result

def mtrx_exp(m, n, p):
    if p == 0:
        return [[1 if i == j else 0 for i in range(n)] for j in range(n)]
    if p % 2 == 1:
        return multiplication(mtrx_exp(m, n, p - 1), m, n, n, n)
    else:
        m = mtrx_exp(m, n, p // 2)
        return multiplication(m, m, n, n, n)


d = 10**9 + 7
k, n = [int(e) for e in input().split()]
fi = [[int(e)] for e in input().split()]
ai = [int(e) for e in input().split()]
if n < k:
    outmat = fi[n][0]
    s = sum([fi[i][0] for i in range(n + 1)])
else:
    outmat, s = 0, sum([fi[i][0] for i in range(k - 1)]) % d
    mtrx = [ai]
    ai.append(0)
    fi.reverse()
    fi.append([s])
    for i in range(k - 1):
        row = [0 for _ in range(k + 1)]
        row[i] = 1
        mtrx.append(row)
    row = [1 if i in [0, k] else 0 for i in range(k + 1)]
    mtrx.append(row)
    values = multiplication(
        mtrx_exp(mtrx, k + 1, n - k + 1), fi, k + 1, 1, k + 1
    )
    outmat = values[0][0]
    s = values[k][0] + outmat
print(outmat % d, s % d)
