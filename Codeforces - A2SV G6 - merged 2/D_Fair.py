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


dist=[[10**9]*k for _ in range(n)]

for g in range(k):
    q=deque()

    for i in range(n):
        if goods[i]==g+1:
            dist[i][g]=0
            q.append(i)
    while q:
        u=q.popleft()
        for v in graph[u]:
            if dist[v][g]>dist[u][g]+1:
                dist[v][g]=dist[u][g]+1
                q.append(v)


ans=[]
for i in range(n):
    dist[i].sort()
    total=sum(dist[i][:s])
    ans.append(str(total))
print(" ".join(ans))
