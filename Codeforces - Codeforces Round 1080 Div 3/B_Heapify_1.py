import sys

input = sys.stdin.readline

t = int(input())

a = list(range(200001))
sz = [1] * 200001

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

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, n + 1):
        a[i] = i
        sz[i] = 1

    for i in range(1, n + 1):
        if i * 2 <= n:
            union(i, i * 2)

    pos = {}
    val = {}

    for i in range(1, n + 1):
        r = find(i)
        pos.setdefault(r, []).append(i)
        val.setdefault(r, []).append(arr[i - 1])

    ok = True
    for r in pos:
        if sorted(pos[r]) != sorted(val[r]):
            ok = False
            break

    print("YES" if ok else "NO")