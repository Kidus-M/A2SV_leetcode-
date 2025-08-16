from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
edges=[]
for _ in range(m):
    u,v=map(int,input().split())
    edges.append((u,v))

l,h, ans=1,m,-1

indegree=[0]*(n+1)
g=[[] for _ in range(n+1)]

for k,(u,v) in enumerate(edges,start=1):
    g[u].append(v)
    indegree[v]+=1
    indg=indegree[:]
    q = deque([i for i in range(1, n + 1) if indg[i] == 0])
    count=0
    unique=True


    while q:
        if len(q)>1:
            unique=False
            break
        u=q.popleft()
        count +=1
        for v in g[u]:
            indegree[v]-=1
            if indegree[v]==0:
                q.append(v)

    if unique and count==n:
        print(k)
        break
else:
    print(-1)
