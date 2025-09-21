import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    vals = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    rg = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        g[u].append(v)
        rg[v].append(u)



    vis = [0]*n
    order = []


    for i in range(n):
        if vis[i]: continue
        stack = [(i, 0)]
        while stack:
            u, state = stack.pop()
            if state == 0:
                if vis[u]: continue
                vis[u] = 1
                stack.append((u,1))
                for v in g[u]:
                    if not vis[v]:
                        stack.append((v,0))
            else:
                order.append(u)

    comp = [-1]*n
    cid = 0


    for u in reversed(order):
        if comp[u] != -1: continue
        stack = [u]
        comp[u] = cid
        while stack:
            x = stack.pop()
            for v in rg[x]:
                if comp[v] == -1:
                    comp[v] = cid
                    stack.append(v)
        cid += 1

    sz = [0]*cid
    sm = [0]*cid
    for i in range(n):
        sz[comp[i]] += 1
        sm[comp[i]] += vals[i]

    dag = [[] for _ in range(cid)]
    indeg = [0]*cid
    for u in range(n):
        for v in g[u]:
            if comp[u] != comp[v]:
                dag[comp[u]].append(comp[v])
    for i in range(cid):
        dag[i] = list(set(dag[i]))
        for v in dag[i]:
            indeg[v] += 1

    dp_len = [0]*cid
    dp_sum = [10**20]*cid
    q = deque()
    for i in range(cid):
        if indeg[i] == 0:
            dp_len[i] = sz[i]
            dp_sum[i] = sm[i]
            q.append(i)
    while q:
        u = q.popleft()
        for v in dag[u]:
            cand_len = dp_len[u] + sz[v]
            cand_sum = dp_sum[u] + sm[v]
            if cand_len > dp_len[v]:
                dp_len[v] = cand_len
                dp_sum[v] = cand_sum
            elif cand_len == dp_len[v] and cand_sum < dp_sum[v]:
                dp_sum[v] = cand_sum
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    ans_len = max(dp_len)
    ans_sum = min(dp_sum[i] for i in range(cid) if dp_len[i] == ans_len)
    print(ans_len, ans_sum)
