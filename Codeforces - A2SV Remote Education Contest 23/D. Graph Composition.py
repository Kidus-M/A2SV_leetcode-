from collections import deque
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

    fc=[-1] *(n+1)
    cid=0


    for i in range(1,n+1):
        if fc[i]==-1:
            q=deque([i])
            fc[i]=cid
            while q:
                u=q.popleft()
                for v in gf[u]:
                    if fc[v]==-1:
                        fc[v]=cid
                        q.append(v)

            cid+=1


    visited = [False]*(n+1)
    ans=0

    for i in range(1, n+1):
        if not visited[i]:
            q=deque([i])
            visited[i]=True
            fseen=set()
            fseen.add(fc[i])

            while q:
                u=q.popleft()
                for v in gg[u]:
                    if not visited[v]:
                        visited[v]=True
                        fseen.add(fc[v])
                        q.append(v)

            ans += len(fseen)-1
    print(ans)






