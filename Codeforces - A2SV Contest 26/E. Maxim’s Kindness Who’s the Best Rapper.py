from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
edges=[]
indegree=[0]*(n+1)
idx={}
g=[[] for _ in range(n+1)]
for i in range(1,m+1):
    u,v=map(int,input().split())
    edges.append((u,v))
    g[u].append(v)
    indegree[v]+=1
    idx[(u,v)]=i
q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
order=[]
unique=True
while q:
    if len(q)>1:
        unique=False
        break
    u=q.popleft()
    order.append(u)
    
    for v in g[u]:
        indegree[v]-=1
        if indegree[v]==0:
            q.append(v)

if len(order)!=n or not unique:
    print(-1)
else:
    ans=0
    for i in range(n-1):
        u,v=order[i],order[i+1]
        ans=max(ans,idx[(u,v)])
    print(ans)
