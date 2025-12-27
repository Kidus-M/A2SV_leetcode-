import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    res = []

    power = 10
    for _ in range(1, 19):
        d = power + 1
        if d > n:
            break
        if n % d == 0:
            res.append(n // d)
        power *= 10
    if not res:
        print(0)
    else:
        res.sort()
        print(len(res))
        print(*res)
