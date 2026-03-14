t = int(input())
for _ in range(t):
    n = int(input())
    c = [0]*n
    p = [0]*n

    for i in range(n):
        x, y = map(int, input().split())
        c[i] = x
        p[i] = y

    f = 0.0
    i = n-1
    while i >= 0:
        m = 1.0 - p[i]/100.0
        v = c[i] + m*f
        if v > f:
            f = v
        i -= 1

    print("%.10f" % f)