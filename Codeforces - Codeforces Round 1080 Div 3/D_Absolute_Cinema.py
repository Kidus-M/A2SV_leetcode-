t = int(input())
for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))

    d = [0] * (n - 1)
    for i in range(n - 1):
        d[i] = f[i + 1] - f[i]

    a = [0] * n
    for i in range(1, n - 1):
        a[i] = (d[i] - d[i - 1]) // 2

    mid_sum = sum(a[1:n-1])
    a[0] = (d[0] + mid_sum) // -2
    a[n - 1] = -sum(a[:n - 1])

    print(*a)