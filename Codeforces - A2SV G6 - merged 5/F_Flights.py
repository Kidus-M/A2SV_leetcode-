from collections import deque
import sys


input=sys.stdin.readline

n,m=map(int,input().split())
edges=[]
graph=[[] for _ in range(n+1)]
revadj=[[] for _ in range(n+1)]

for i in range(m):
    u,v=map(int,input().split())
    edges.append((u,v))
    graph[u].append(v)
    revadj[v].append(u)


can_reach=[False]*(n+1)


indegree=[0]*(n+1)
for u in range(1,n+1):
    for v in graph[u]:
        indegree[v]+=1

q=deque()
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

topo=[]
while q:
    u=q.popleft()
    topo.append(u)
    for v in graph[u]:
        indegree[v]-=1
        if indegree[v]==0:
            q.append(v)


mindist=[float('inf')]*(n+1)
maxdist=[-float('inf')]*(n+1)

mindist[1]=maxdist[1]=0
for u in topo:
    for v in graph[u]:
        mindist[v]=min(mindist[v],mindist[u]+1)
        maxdist[u]=max(maxdist[u],maxdist[v]+1)

if mindist[n]==maxdist[n]:
    print("NO")
    exit()

ans=[]
for u,v in edges:
    if mindist[v]==mindist[u]+1:
        ans.append(1)
    else:
        ans.append(2)

print("YES")
for a in ans:
    print(a)