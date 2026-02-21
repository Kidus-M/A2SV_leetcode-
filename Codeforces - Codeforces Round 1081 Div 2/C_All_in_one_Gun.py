t = int(input())

for _ in range(t):
    x = input().split()
    while len(x) < 3:
        x += input().split()

    n = int(x[0])
    h = int(x[1])
    k = int(x[2])

    a = []
    while len(a) < n:
        a += list(map(int, input().split()))

    p = [0] * n
    mn = [0] * n

    p[0] = a[0]
    mn[0] = a[0]
    i = 1
    while i < n:
        p[i] = p[i - 1] + a[i]
        if mn[i - 1] < a[i]:
            mn[i] = mn[i - 1]
        else:
            mn[i] = a[i]
        i += 1

    mx = [0] * n
    mx[n - 1] = a[n - 1]
    i = n - 2
    while i >= 0:
        if mx[i + 1] > a[i]:
            mx[i] = mx[i + 1]
        else:
            mx[i] = a[i]
        i -= 1

    s = p[n - 1]
    ans = 10**30

    i = 1
    while i <= n:
        if i < n:
            d = mx[i] - mn[i - 1]
            if d < 0:
                d = 0
            cur = p[i - 1] + d
        else:
            cur = s

        r = h - cur
        if r <= 0:
            m = 0
        else:
            m = (r + s - 1) // s

        tm = m * (n + k) + i
        if tm < ans:
            ans = tm

        i += 1

    print(ans)