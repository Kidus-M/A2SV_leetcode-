import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    lc = [-1] * n
    rc = [-1] * n
    par = [-1] * n

    st = []
    root = -1

    for i in range(n):
        gone = -1
        while st and a[st[-1]] < a[i]:
            gone = st.pop()

        lc[i] = gone
        if gone != -1:
            par[gone] = i

        if st:
            rc[st[-1]] = i
            par[i] = st[-1]
        else:
            root = i
            par[i] = -1

        st.append(i)

    dp = [1] * n
    need = [0] * n

    for i in range(n):
        if lc[i] != -1:
            need[i] += 1
        if rc[i] != -1:
            need[i] += 1

    q = deque()
    for i in range(n):
        if need[i] == 0:
            q.append(i)

    while q:
        u = q.popleft()
        if par[u] != -1:
            p = par[u]
            if dp[u] + 1 > dp[p]:
                dp[p] = dp[u] + 1
            need[p] -= 1
            if need[p] == 0:
                q.append(p)

    print(n - dp[root])