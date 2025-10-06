from collections import deque
n,m=map(int,input().split())
rail=[[0]*n for _ in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    rail[u-1][v-1]=rail[v-1][u-1]=1
roads=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j and rail[i][j]==0:
            roads[i][j]=1
dist1=[-1]*n
q=deque([0]); dist1[0]=0
while q:
    u=q.popleft()
    for v in range(n):
        if rail[u][v] and dist1[v]==-1:
            dist1[v]=dist1[u]+1
            q.append(v)
dist2=[-1]*n
q=deque([0]); dist2[0]=0
while q:
    u=q.popleft()
    for v in range(n):
        if roads[u][v] and dist2[v]==-1:
            dist2[v]=dist2[u]+1
            q.append(v)
if dist1[n-1]==-1 or dist2[n-1]==-1:
    print(-1)
else:
    print(max(dist1[n-1],dist2[n-1]))
