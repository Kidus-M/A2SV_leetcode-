from collections import deque, defaultdict
t=int(input())

for _ in range(t):
    n, m1, m2 = map(int, input().split())
    gf = [[] for _ in range(n + 1)]
    gg = [[] for _ in range(n + 1)]
    fedge=set()
    for _ in range(m1):
        u,v=map(int, input().split())
        gf[u].append(v)
        gf[v].append(u)
        fedge.add((min(u,v), max(u,v)))

    for _ in range(m2):
        u,v=map(int, input().split())
        gg[u].append(v)
        gg[v].append(u)

    component=[0] * (n+1)
    for i in range(1,n+1):
        if component[i]==0:
            q=deque([i])
            component[i]=i
            while q:
                u=q.popleft()
                for v in gg[u]:
                    if component[v]==0:
                        component[v]=i
                        q.append(v)

    ans=0
    for u in range(1, n+1):
        for v in range(u+1, n+1):
            same=(component[u]==component[v])
            exist=(u,v) in fedge
            if same and not exist:
                ans += 1
            elif not same and exist:
                ans += 1


    print(ans)










