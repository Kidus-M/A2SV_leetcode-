def nCr(n, r):
    if r == 0:
        return 1
    if r == 1:
        return n

    return nCr(n, r - 1) * (n - r + 1) // r


n = 5
r = 2


print(nCr(n, r))