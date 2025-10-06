import heapq
import sys


input=sys.stdin.readline


n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,w=map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))


INF=float("inf")
dist=[INF]*(n+1)
parent=[-1]*(n+1)


dist[1]=0
q=[(0,1)]

while q:
    d,u=heapq.heappop(q)
    if d>dist[u]:
        continue
    for v,w in graph[u]:
        if dist[u]+w<dist[v]:
            dist[v]=dist[u]+w
            parent[v]=u
            heapq.heappush(q,(dist[v],v))


if dist[n]==INF:
    print(-1)
else:
    path=[]
    curr=n
    while curr !=-1:
        path.append(curr)
        curr=parent[curr]
    print(*reversed(path))


