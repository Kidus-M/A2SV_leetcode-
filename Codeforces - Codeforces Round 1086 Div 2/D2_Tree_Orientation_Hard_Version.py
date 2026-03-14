from collections import deque

t = int(input())
P = [1 << i for i in range(8005)]

for _ in range(t):
    n = int(input())
    rows = [input().strip() for _ in range(n)]

    valid = True
    for i in range(n):
        if rows[i][i] != '1':
            valid = False
            break
    if not valid:
        print("No")
        continue

    masks = [int(rows[i][::-1], 2) for i in range(n)]
    D = [rows[i].count('1') for i in range(n)]

    edges = []

    for u in range(n):
        c = masks[u] & ~P[u]
        a = [j for j in range(n) if rows[u][j] == '1' and j != u]
        a.sort(key=lambda x: D[x], reverse=True)

        for v in a:
            if c & P[v]:
                if (masks[u] & masks[v]) != masks[v]:
                    valid = False
                    break
                edges.append((u, v))
                if len(edges) >= n:
                    valid = False
                    break
                c &= ~masks[v]

        if not valid or c != 0:
            valid = False
            break

    if not valid or len(edges) != n - 1:
        print("No")
        continue

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    vis = [0] * n
    q = deque([0])
    vis[0] = 1
    cnt = 1

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if not vis[nxt]:
                vis[nxt] = 1
                q.append(nxt)
                cnt += 1

    if cnt != n:
        print("No")
    else:
        print("Yes")
        for u, v in edges:
            print(u + 1, v + 1)