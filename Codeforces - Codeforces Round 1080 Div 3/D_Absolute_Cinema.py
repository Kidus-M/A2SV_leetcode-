import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))

    d = [f[i + 1] - f[i] for i in range(n - 1)]
    a = [0] * n

    for i in range(1, n - 1):
        a[i] = (d[i] - d[i - 1]) // 2

    mid_sum = sum(a[1:n-1])

    known = 0
    for i in range(1, n - 1):
        known += a[i] * i

    a[n - 1] = (f[0] - known) // (n - 1)
    #print(a[n-1])
    a[0] = d[0] + mid_sum + a[n - 1]

    print(*a)
