import sys

input = sys.stdin.readline

def find(x):
    while a[x] != x:
        a[x] = a[a[x]]
        x = a[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if sz[x] < sz[y]:
            x, y = y, x
        a[y] = x
        sz[x] += sz[y]

t = int(input())

a = list(range(200001))
sz = [1] * 200001

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, n + 1):
        a[i] = i
        sz[i] = 1

    for i in range(1, n + 1):
        if i * 2 <= n:
            union(i, i * 2)

    grp = {}

    for i in range(1, n + 1):
        r = find(i)
        if r not in grp:
            grp[r] = [[], []]
        grp[r][0].append(i)
        grp[r][1].append(arr[i - 1])

    ok = True
    for g in grp.values():
        if sorted(g[0]) != sorted(g[1]):
            ok = False
            break

    print("YES" if ok else "NO")