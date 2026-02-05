import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    ans = [0] * (n + 1)

    # stack: (node, parent, depth, pref, min_pref, max_pref)
    stack = [(1, 0, 0, 0, 0, 0)]

    while stack:
        u, parent, depth, pref, min_pref, max_pref = stack.pop()

        # compute b[u]
        if depth % 2 == 0:
            pref_u = pref + a[u]
            ans[u] = pref_u - min_pref
        else:
            pref_u = pref - a[u]
            ans[u] = max_pref - pref_u

        new_min = min(min_pref, pref_u)
        new_max = max(max_pref, pref_u)

        for v in adj[u]:
            if v != parent:
                stack.append((v, u, depth + 1, pref_u, new_min, new_max))

    print(*ans[1:])
