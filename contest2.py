from collections import deque, defaultdict
t=int(input())

for _ in range(t):
    n, m1, m2 = map(int, input().split())
    gf = [[] for _ in range(n + 1)]
    gg = [[] for _ in range(n + 1)]

    for _ in range(m1):
        u,v=map(int, input().split())
        gf[u].append(v)
        gf[v].append(u)

    for _ in range(m2):
        u,v=map(int, input().split())
        gg[u].append(v)
        gg[v].append(u)



    fc=[0] *(n+1)
    cid=0
    for i in range(1,n+1):
        if fc[i]==0:
            cid += 1
            q=deque([i])
            fc[i]=cid
            while q:
                u=q.popleft()
                for v in gf[u]:
                    if fc[v]==0:
                        fc[v]=cid
                        q.append(v)

    gc = [0] * (n + 1)
    cid = 0
    for i in range(1,n+1):
        if gc[i]==0:
            cid += 1
            q=deque([i])
            gc[i]=cid
            while q:
                u=q.popleft()
                for v in gg[u]:
                    if gc[v]==0:
                        gc[v]=cid
                        q.append(v)





    gtf=defaultdict(set)
    for i in range(i,n+1):
        gtf[gc[i]].add(fc[i])

    addops=sum(len(s) for s in gtf.values())

    ftg = defaultdict(set)
    for i in range(i, n + 1):
        ftg[fc[i]].add(gc[i])

    delops=0
    for u in range(1,n+1):
        for v in gf[u]:
            if v>u:
                if gc[u] !=gc[v]:
                    delops += 1

    ans=delops
    print(ans)








