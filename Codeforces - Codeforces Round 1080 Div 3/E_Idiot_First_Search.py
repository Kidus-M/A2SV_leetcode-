import sys

input = sys.stdin.readline
MOD = 10**9 + 7

t = int(input())

for _ in range(t):
    n = int(input())

    l = [0] * (n + 1)
    r = [0] * (n + 1)
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        li, ri = map(int, input().split())
        l[i] = li
        r[i] = ri
        if li != 0:
            parent[li] = i
        if ri != 0:
            parent[ri] = i

    # recussion never works with python
    order = []
    stack = [1]

    while stack:
        u = stack.pop()
        order.append(u)
        if l[u] != 0:
            stack.append(l[u])
        if r[u] != 0:
            stack.append(r[u])

    T = [0] * (n + 1)
    for u in reversed(order):
        if l[u] == 0 and r[u] == 0:
            T[u] = 1
        else:
            T[u] = (T[l[u]] + T[r[u]] + 3) % MOD

    ans = [0] * (n + 1)

    for u in order:
        if u == 1:
            ans[u] = T[u]
        else:
            ans[u] = (ans[parent[u]] + T[u]) % MOD

    print(*ans[1:])
