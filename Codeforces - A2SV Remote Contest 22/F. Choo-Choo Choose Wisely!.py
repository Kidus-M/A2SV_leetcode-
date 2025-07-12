from collections import defaultdict
import heapq
import sys
input=sys.stdin.readline


n,m,k=map(int,input().split())
graph=defaultdict(list)

for _ in range(m):
    u,v,x=map(int,input().split())
    graph[u].append((v,x,False))
    graph[v].append((u,x,False))
trainR=[]
for _ in range(k):
    s,y=map(int,input().split())
    graph[1].append((s,y,True))
    graph[s].append((1,y,True))
    trainR.append((s,y))


dist=[float('inf')] * (n+1)
dist[1]=0
pq=[(0,1)]


while pq:
    d,u=heapq.heappop(pq)
    if d>dist[u]:
        continue
    for v,w, _ in graph[u]:
        if dist[v]>dist[u]+w:
            dist[v]=dist[u]+w
            heapq.heappush(pq,(dist[v],v))



needed=[False] * (n+1)
for u in range(1,n+1):
    for v,w,ist in graph[u]:
        if not ist and dist[v]==dist[u]+w:
            needed[v]=True



ans=0
used=[False]*(n+1)
for s,y in trainR:
    if y >dist[s]:
        ans +=1
    elif y==dist[s]:
        if used[s] or needed[s]:
            ans += 1
        else:
            used[s]=True
print(ans)