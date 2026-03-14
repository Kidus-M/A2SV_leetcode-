from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())

    a = []
    for i in range(n):
        row = list(map(int, input().split()))
        a += row

    c = Counter(a)
    mx = 0
    for v in c.values():
        if v > mx:
            mx = v

    lim = n*(n-1)

    if mx > lim:
        print("NO")
    else:
        print("YES")