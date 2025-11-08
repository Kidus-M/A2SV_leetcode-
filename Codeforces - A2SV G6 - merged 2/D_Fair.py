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


dist=[]

for g in range(1,k+1):
    q=deque()
    d=[-1]*n
    for i in range(n):
        if goods[i]==g:
            d[i]=0
            q.append(i)
    while q:
        u=q.popleft()

        for v in graph[u]:
            if d[v]==-1:
                d[v]=d[u]+1
                q.append(v)
    dist.append(d)

ans=[]
for i in range(n):
    dd=[dist[g][i] for g in range(k)]
    dd.sort()
    ans.append(str(sum(dd[:s])))
print(" ".join(ans))
