from collections import deque
import sys


input=sys.stdin.readline
n,m,k,s=map(int,input().split())
goods=list(map(int,input().split()))
graph=[[]for _ in range(n)]



for _ in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    graph[u].append(v)
    graph[v].append(u)


dist=[[] for _ in range(n)]

for g in range(1,k+1):
    q=deque()
    visited=[-1]*n
    for i in range(n):
        if goods[i]==g:
            visited[i]=0
            q.append(i)
    while q:
        u=q.popleft()
        for v in graph[u]:
            if visited[v]==-1:
                visited[v]=visited[u]+1
                q.append(v)
    for i in range(n):
        if visited[i]!=-1:
            dist[i].append(visited[i])


ans=[]
for i in range(n):
    dist[i].sort()
    total=sum(dist[i][:s])
    ans.append(str(total))
print(" ".join(ans))
