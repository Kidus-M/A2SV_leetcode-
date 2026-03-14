from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    r = []
    for i in range(n):
        s = input().strip()
        r.append([int(c) for c in s])

    ok = True
    for i in range(n):
        if r[i][i] != 1:
            ok = False
        for j in range(i + 1, n):
            if r[i][j] == 1 and r[j][i] == 1:
                ok = False
    if not ok:
        print("No")
        continue

    g = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and r[i][j]:
                g[i].append(j)

    e = []
    for i in range(n):
        for j in g[i]:
            d = True
            for k in g[i]:
                if k != j and r[k][j]:
                    d = False
                    break
            if d:
                e.append((i + 1, j + 1))

    if len(e) != n - 1:
        print("No")
        continue

    d = [[] for _ in range(n)]
    u = [[] for _ in range(n)]
    for x, y in e:
        a = x - 1
        b = y - 1
        d[a].append(b)
        u[a].append(b)
        u[b].append(a)

    vis = [0] * n
    q = deque([0])
    vis[0] = 1
    while q:
        x = q.popleft()
        for y in u[x]:
            if not vis[y]:
                vis[y] = 1
                q.append(y)
    if not all(vis):
        print("No")
        continue

    def go(s):
        v = [0] * n
        q = deque([s])
        v[s] = 1
        while q:
            x = q.popleft()
            for y in d[x]:
                if not v[y]:
                    v[y] = 1
                    q.append(y)
        return v

    good = True
    for i in range(n):
        v = go(i)
        for j in range(n):
            if v[j] != (r[i][j] == 1):
                good = False
                break
        if not good:
            break

    if good:
        print("Yes")
        for x, y in e:
            print(x, y)
    else:
        print("No")