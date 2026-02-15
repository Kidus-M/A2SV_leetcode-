import sys

input = sys.stdin.readline
INF = 10**9

adj = [[] for _ in range(7)]
for i in range(1, 7):
    for j in range(1, 7):
        if i != j and i + j != 7:
            adj[i].append(j)

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [INF] * 7
    for v in range(1, 7):
        dp[v] = 0 if v == a[0] else 1

    for i in range(1, n):
        ndp = [INF] * 7
        for v in range(1, 7):
            best = INF
            for u in adj[v]:
                if dp[u] < best:
                    best = dp[u]
            ndp[v] = best + (v != a[i])
        dp = ndp

    print(min(dp[1:]))